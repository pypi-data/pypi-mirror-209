import json
from typing import Any

from adjudicator import get
from equilibrium import Resource

from helsing.scm.resources.v1alpha.AwsAccount import AwsAccount
from helsing.scm.resources.v1alpha.TerraformWorkspace import Expression, ProviderFrom, Variable
from helsing.scm.tfcodegen.aws.create_account import AwsAccountCreationCode
from helsing.scm.tfcodegen.tfe.account_service import TerraformAccountService
from helsing.scm.utils.templating import template


class AwsAccountService(TerraformAccountService, resourceType=AwsAccount):
    """
    The implementation for exposing AWS account credentials to a Terraform workspace.
    """

    def get_variables(self, resource: Resource[object]) -> list[Variable]:
        code = get(AwsAccountCreationCode, {Resource[AwsAccount]: resource.into(AwsAccount)})
        return [
            Variable(
                name="aws_account_id",
                value=Expression(f"{code.module_address}.account_id"),
                category="Terraform",
                hcl=False,
                sensitive=False,
            ),
            Variable(
                name="aws_assume_role_arn",
                value=Expression(f"{code.module_address}.admin_role_arn"),
                category="Terraform",
                hcl=False,
                sensitive=False,
            ),
            Variable(
                name="AWS_ACCESS_KEY_ID",
                value=Expression(f"{code.module_address}.access_key"),
                category="Env",
                hcl=False,
                sensitive=True,
            ),
            Variable(
                name="AWS_SECRET_ACCESS_KEY",
                value=Expression(f"{code.module_address}.secret_key"),
                category="Env",
                hcl=False,
                sensitive=True,
            ),
        ]

    def get_provider_initialization(self, provider_from: ProviderFrom, resource: Resource[Any]) -> str:
        aws_account = resource.into(AwsAccount)
        return template(
            """
            provider "aws" {
                % if provider_from.alias:
                alias = ${dumps(provider_from.alias) or "null"}
                % endif
                region = "${aws_account.spec.defaultRegion}"
                allowed_account_ids = [var.aws_account_id]
                assume_role {
                    role_arn = var.aws_assume_role_arn
                }
            }
            """,
            "dedent",
            dumps=json.dumps,
            aws_account=aws_account,
            provider_from=provider_from,
        )
