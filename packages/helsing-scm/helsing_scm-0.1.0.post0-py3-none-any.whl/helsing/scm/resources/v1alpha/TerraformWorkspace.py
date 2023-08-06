from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

from equilibrium import Resource

from helsing.scm import DOMAIN


@dataclass(frozen=True)
class ProviderFrom:
    """
    Represents a reference to another resource that must be supported as a source for credentials and the generation
    of initialization code for a Terraform provider.
    """

    #: The reference to the resource.
    accountRef: Resource.URI

    #: The version of the provider to use. If this is not set, no version will be set in the generated code.
    #: The provider type is fixed by the type of resource referenced with #accountRef.
    providerVersion: str | None = None

    #: An optional alias for the provider.
    alias: str | None = None


@dataclass(frozen=True)
class Variable:
    """
    Represents a Terraform variable that will be assigned to a Terraform workspace.
    """

    #: The name of the variable.
    name: str

    #: The value of the variable.
    value: str | Expression

    #: An optional description of the variable.
    description: str | None = None

    #: Whether the variable is sensitive.
    sensitive: bool = False

    #: The category of the variable.
    category: Literal["Terraform", "Env"] = "Terraform"

    #: Whether the value is in HCL format.
    hcl: bool = False


@dataclass
class Expression:
    """
    Represents an expression of Terraform code.
    """

    #: The expression.
    value: str

    type: Literal["Expression"] = "Expression"


@dataclass(frozen=True)
class ApiDrivenWorkflow:
    """
    Represents API-driven Terraform Workspace run workflow as described here:

    https://developer.hashicorp.com/terraform/cloud-docs/run/api
    """

    #: A reference to a Terraform module. This can be a module from a a Git repository. In Terraform, a Git repository
    #: must be prefixed with "git::", but here we can determine that a Git repository is referenced by a simpler URL
    #: format, such as simply `git@github:my-org/my-repo`.
    moduleSource: str

    #: The version of the module to use. If a Git module is specified with #moduleSource, this must be a Git reference
    #: or commit and will be appended to the module source URL with a `?ref=` query parameter.
    moduleVersion: str | None = None

    #: A list of resources from which to source provider credentials and initialization code.
    providersFrom: list[ProviderFrom] = field(default_factory=list)

    #: A list of variables to assign to the workspace and to forward as inputs to the Terraform module. These variables
    #: should not conflict with variables specified in the #TerraformWorkspace.variables list.
    variables: list[Variable] = field(default_factory=list)

    type: Literal["ApiDriven"] = "ApiDriven"


@dataclass(frozen=True)
class TerraformWorkspace(Resource.Spec, apiVersion=f"{DOMAIN}/v1alpha1", kind="TerraformWorkspace", namespaced=False):
    """
    Represents a Terraorm workspace which may be given access to an AWS account.
    """

    #: The name of the Terraform workspace.
    workspaceName: str

    #: The type of workflow that the workspace is using to manage infrastructure,
    workflow: ApiDrivenWorkflow

    #: A list of variables that will be assigned to the Terraform workspace. The variable will not be considerted
    #: further. For API-driven workflows, variables that should also be forwarded to the instantiated Terraform module,
    #: they must be specified in the #ApiDrivenWorkflow.variables list.
    variables: list[Variable] = field(default_factory=list)
