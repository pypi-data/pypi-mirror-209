from abc import abstractmethod
from typing import Any

from equilibrium import Resource, Service

from helsing.scm import DOMAIN
from helsing.scm.resources.v1alpha.TerraformWorkspace import ProviderFrom, Variable


class TerraformAccountService(Service, serviceId=f"{DOMAIN}/v1alpha1/TerraformAccountService"):
    """
    This service provides an API to retrieve Terraform workspace configuration for a resource that resembles a
    Cloud "account". It is used for resources referenced in #ApiDrivenWorkflow.providersFrom to expose credentials
    in a workspace.

    Using this service, a Terraform workspace can be configured to use the credentials of a resource for which
    an implementation of this service exists without the Terraform workspace code generation to having to understand
    the resource type. This allows us to extend the set of Cloud account resources that a Terraform workspace can
    consume credentials from in the future.
    """

    @abstractmethod
    def get_variables(self, resource: Resource[Any]) -> list[Variable]:
        """
        Return a list of variables that should be assigned to the Terraform workspace, which are derived from
        the specified resource.
        """

    @abstractmethod
    def get_provider_initialization(self, provider_from: ProviderFrom, resource: Resource[Any]) -> str:
        """
        Return the code that will be put into an API-driven Terrafork workspace to initialize the provider for
        the specified resource.
        """
