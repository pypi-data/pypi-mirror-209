"""
Implements the Terraform code generation for AWS accounts.
"""

import json
from dataclasses import dataclass
from string import Template

from adjudicator import Rule, collect_rules, rule
from equilibrium import Resource, ResourceContext

from helsing.scm.resources.v1alpha.AwsAccount import AwsAccount
from helsing.scm.utils.templating import template

from .settings import AwsTerraformCodegenSettings


@dataclass(frozen=True)
class AwsAccountCreationCode:
    #: The generated code.
    value: str

    #: The address of the AWS module resource that was generated in the code.
    module_address: str


def render_template_string(aws_account: Resource[AwsAccount], template: str) -> str:
    return Template(template).substitute(identifier=aws_account.metadata.name)


@rule
def create_aws_account(context: ResourceContext, aws_account: Resource[AwsAccount]) -> AwsAccountCreationCode:
    """
    Generate Terraform code that creates an AWS account and stores its credentials in Vault.
    """

    assert aws_account.metadata.namespace is not None
    config = AwsTerraformCodegenSettings.get(context, namespace=aws_account.metadata.namespace)
    module = config.spec.terraformModule.as_terraform_module()

    normalized_name = aws_account.metadata.name.replace("-", "_")

    code = template(
        """
        module "aws_account_${normalized_name}" {
            source = "${module.source}"
            % if module.version:
            version = "${module.version}"
            % endif
            account_name = "${aws_account.spec.accountName}"
            account_email = "${aws_account.spec.accountEmail}"
            organizational_unit = "${aws_account.spec.organizationalUnit}"
            % for key, value in module.additionalInputVariables.items():
            ${key} = ${dumps(render_template_string(aws_account, value)) if isinstance(value, str) else dumps(value)}
            % endfor
        }
        """,
        "dedent",
        dumps=json.dumps,
        render_template_string=render_template_string,
        module=module,
        aws_account=aws_account,
        config=config,
        normalized_name=normalized_name,
    )

    return AwsAccountCreationCode(value=code, module_address=f"module.aws_account_{normalized_name}")


def get_rules() -> list[Rule]:
    return collect_rules()
