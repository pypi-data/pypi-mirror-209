"""
Implements the configuration spec for AWS accounts.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal, Sequence

from equilibrium import Resource, ResourceContext

from helsing.scm import DOMAIN, GIT_REPOSITORY_URL
from helsing.scm.utils.develop import get_develop_root
from helsing.scm.utils.types import FrozenDict, HashableMapping

# TODO(@NiklasRosenstein): Databind will deserialize Sequence as a list; but we'd actually
#       want that to be an immutable sequence type. We should maybe update databind to support this.
JsonValue = str | int | float | bool | FrozenDict[str, Any] | Sequence[Any]


@dataclass(frozen=True)
class ScmModule:
    """
    Reference a Terraform module that is available as part of the SCM, either referenced from the local filesystem
    (only possible when SCM is installed in Python develop mode) or from the GitHub repository.
    """

    #: The name of the Terraform module in the SCM `modules/` directory.
    name: str

    #: Where to source the SCM module from.
    source: Literal["Local", "Remote"] = "Remote"

    #: The Git ref to use when sourcing the module from the SCM repository. This is only used when `source` is `Remote`.
    ref: str | None = None

    #: Additional static input variables to set when the module is instantiated.
    additionalInputVariables: HashableMapping[str, JsonValue] = field(default_factory=FrozenDict)

    type: Literal["ScmModule"] = "ScmModule"

    def as_terraform_module(self) -> TerraformModule:
        """
        Convert this SCM module to a Terraform module.
        """

        match self.source:
            case "Local":
                source = str(get_develop_root() / "modules" / self.name)
            case "Remote":
                source = f"git::{GIT_REPOSITORY_URL}//modules/{self.name}"
                if self.ref is not None:
                    source += f"?ref={self.ref}"
            case _:
                raise ValueError(f"Invalid source {self.source!r}")

        return TerraformModule(
            source=source,
            version=None,
            additionalInputVariables=self.additionalInputVariables,
        )


@dataclass(frozen=True)
class TerraformModule:
    """
    Reference a Terraform module that is available from the Terraform registry or from a Git repository.
    """

    #: The Terraform module source. This must be the full string that you would also set in the `source`
    #: attribute of the `module {}` block.
    source: str

    #: The version of the Terraform module to use.
    version: str | None = None

    #: Additional static input variables to set when the module is instantiated.
    additionalInputVariables: HashableMapping[str, JsonValue] = field(default_factory=FrozenDict)

    type: Literal["Terraform"] = "Terraform"

    def as_terraform_module(self) -> TerraformModule:
        return self


@dataclass(frozen=True)
class AwsTerraformCodegenSettings(
    Resource.Spec,
    apiVersion=f"{DOMAIN}/v1alpha1",
    kind="AwsTerraformCodegenSettings",
    namespaced=False,
):
    """
    Contains settings for Terraform code generation related to AWS account creation.
    """

    #: The Terraform module that is used to instantiate the AWS account. The module must have, at minimum, the
    #: following inputs varibales:
    #:
    #: - `account_name`: The name of the account.
    #: - `account_email`: The email address of the account.
    #: - `organizational_unit`: The organizational unit of the account (full name, not the ID).
    #:
    #: The module must output:
    #:
    #: - `account_id`: The AWS account ID.
    #: - `access_key`: The AWS access key.
    #: - `secret_key`: The AWS secret key.
    #: - `admin_role_arn`: The AWS administrator role ARN in the account.
    terraformModule: ScmModule | TerraformModule

    @staticmethod
    def get(context: ResourceContext) -> Resource[AwsTerraformCodegenSettings]:
        resources = context.resources.list(AwsTerraformCodegenSettings)
        if len(resources) == 0:
            raise RuntimeError("No AwsTerraformCodegenSettings resource found.")
        if len(resources) > 1:
            raise RuntimeError("Multiple AwsTerraformCodegenSettings resources found.")
        return resources[0]


def get_resources() -> list[type[Resource.Spec]]:
    return [AwsTerraformCodegenSettings]
