"""
Implements the configuration spec for AWS accounts.
"""

from __future__ import annotations

from dataclasses import dataclass

from equilibrium import Resource, ResourceContext

from helsing.scm import DOMAIN
from helsing.scm.tfcodegen.aws.settings import ScmModule, TerraformModule


@dataclass(frozen=True)
class TerraformWorkspaceCodegenSettings(
    Resource.Spec,
    apiVersion=f"{DOMAIN}/v1alpha1",
    kind="TerraformWorkspaceCodegenSettings",
    namespaced=False,
):
    """
    Contains settings for Terraform code generation related to TFE workspace creation.
    """

    #: The Terraform module that is used to instantiate the AWS account. The module must have, at minimum, the
    #: following inputs varibales:
    #:
    #: - `variables`: A map of variable configurations that are assigned to the workspace. See #Variable.
    #: - `configuration`: A string that represents the Terraform code to execute as part of the workspace.
    terraformModule: ScmModule | TerraformModule

    @staticmethod
    def get(context: ResourceContext) -> Resource[TerraformWorkspaceCodegenSettings]:
        resources = context.resources.list(TerraformWorkspaceCodegenSettings)
        if len(resources) == 0:
            raise RuntimeError("No TerraformWorkspaceCodegenSettings resource found.")
        if len(resources) > 1:
            raise RuntimeError("Multiple TerraformWorkspaceCodegenSettings resources found.")
        return resources[0]


def get_resources() -> list[type[Resource.Spec]]:
    return [TerraformWorkspaceCodegenSettings]
