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
    namespaced=True,
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
    def get(context: ResourceContext, namespace: str) -> Resource[TerraformWorkspaceCodegenSettings]:
        resources = context.resources.list(TerraformWorkspaceCodegenSettings, namespace=namespace)
        if len(resources) == 0:
            raise RuntimeError(f"No TerraformWorkspaceCodegenSettings resource found in {namespace!r}.")
        if len(resources) > 1:
            raise RuntimeError(f"Multiple TerraformWorkspaceCodegenSettings resources found in {namespace!r}.")
        return resources[0]


def get_resources() -> list[type[Resource.Spec]]:
    return [TerraformWorkspaceCodegenSettings]
