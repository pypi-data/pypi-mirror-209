"""
Implements generating Terraform code.
"""

from logging import getLogger
from pathlib import Path

from adjudicator import Rule, get
from equilibrium import Resource, ResourceContext, Service

from helsing.scm.resources.v1alpha.AwsAccount import AwsAccount
from helsing.scm.resources.v1alpha.TerraformWorkspace import TerraformWorkspace
from helsing.scm.tfcodegen import aws, tfe

logger = getLogger(__name__)


def get_rules() -> list[Rule]:
    """
    Return the rules to use for generating Terraform code.
    """

    from . import aws, tfe

    return [
        *aws.get_rules(),
        *tfe.get_rules(),
    ]


def get_services() -> list[Service]:
    """
    Return the services to use for generating Terraform code.
    """

    from . import aws

    return [
        *aws.get_services(),
    ]


def get_resources() -> list[type[Resource.Spec]]:
    """
    Return the resources to use for generating Terraform code.
    """

    from . import aws, tfe

    return [
        *aws.get_resources(),
        *tfe.get_resources(),
    ]


def generate_terraform_code(context: ResourceContext, directory: Path) -> None:
    """
    Generate Terraform code for the given resources in the given directory.
    """

    for aws_account in context.resources.list(AwsAccount):
        aws_code = get(
            aws.create_account.AwsAccountCreationCode,
            {Resource[AwsAccount]: aws_account},
        )
        path = directory / f"aws-account-{aws_account.metadata.name}.tf"
        logger.info("Write '%s'", path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(aws_code.value)

    for tfe_workspace in context.resources.list(TerraformWorkspace):
        tfe_code = get(
            tfe.create_workspace.TerraformWorkspaceCreationCode,
            {Resource[TerraformWorkspace]: tfe_workspace},
        )
        path = directory / f"tfe-workspace-{tfe_workspace.metadata.name}.tf"
        logger.info("Write '%s'", path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(tfe_code.value)
