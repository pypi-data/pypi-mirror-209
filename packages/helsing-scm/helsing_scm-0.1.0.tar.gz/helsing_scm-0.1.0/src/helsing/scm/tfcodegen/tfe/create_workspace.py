import json
from dataclasses import dataclass
from textwrap import indent

from adjudicator import Rule, collect_rules, rule
from equilibrium import Resource, ResourceContext

from helsing.scm import __version__
from helsing.scm.resources.v1alpha.TerraformWorkspace import TerraformWorkspace, Variable
from helsing.scm.tfcodegen.tfe.account_service import TerraformAccountService
from helsing.scm.tfcodegen.tfe.settings import TerraformWorkspaceCodegenSettings
from helsing.scm.utils.templating import template


@dataclass(frozen=True)
class TerraformCodegenConfig:
    """
    Settings for generating code related to the creation of Terraform workspaces.
    """

    #: The module that is used to create the Terraform workspace.
    workspace_module: str = f"git::https://github.com/helsing-ai/scm/modules/tfe_workspace?ref={__version__}"


@dataclass(frozen=True)
class TerraformWorkspaceCreationCode:
    """
    Represents the code that defines a Terraform workspace.
    """

    value: str


@rule
def create_terraform_workspace(
    context: ResourceContext,
    workspace: Resource[TerraformWorkspace],
) -> TerraformWorkspaceCreationCode:
    """
    Generate Terraform code that creates a Terraform workspace using the "tfe" provider.
    """

    settings = TerraformWorkspaceCodegenSettings.get(context)
    terraform_module = settings.spec.terraformModule.as_terraform_module()

    normalized_name = workspace.metadata.name.replace("-", "_")

    variables = list(workspace.spec.variables)
    provider_variables: list[Variable] = []
    provider_snippets: list[str] = []

    # Collect variables and provider initialization code snippets for the resources that the workspace depends on.
    for provider_from in workspace.spec.workflow.providersFrom:
        account = context.resources.get(provider_from.accountRef)
        service: TerraformAccountService = context.services.get(
            provider_from.accountRef.type, TerraformAccountService  # type: ignore[type-abstract]
        )
        provider_variables += service.get_variables(account)
        provider_snippets.append(service.get_provider_initialization(provider_from, account))

    code = template(
        """
        module "workspace_${normalized_name}" {
            source = "${module.source}"
            % if module.version:
            version = "${module.version}"
            % endif
            name = "${workspace.spec.workspaceName}"
            variables = {
            % for variable in variables + provider_variables:
                ${variable.name} = {
                    value = ${dumps(variable.value) if isinstance(variable.value, str) else variable.value.value}
                    % if variable.description:
                    description = "${variable.description}"
                    % endif
                    category = "${variable.category.lower()}"
                    % if variable.sensitive:
                    sensitive = true
                    % endif
                    % if variable.hcl:
                    hcl = true
                    % endif
                }
            % endfor
            }
            configuration = <<-EOF
                % for variable in variables + provider_variables:
                % if variable.category == "Terraform":
                variable "${variable.name}" {${ " sensitive = true " if variable.sensitive else "" }}
                % endif
                % endfor
                % for provider_snippet in provider_snippets:
                ${indent(provider_snippet, " " * 8)}
                % endfor
                module "main" {
                    source = "${workspace.spec.workflow.moduleSource}"
                    % if workspace.spec.workflow.moduleVersion:
                    version = "${workspace.spec.workflow.moduleVersion}"
                    % endif
                    % for variable in variables:
                    ${variable.name} = var.${variable.name}
                    % endfor
                }

                # TODO: Add individual outputs here / but how do we know which?
                output "module" {
                    value = module.main
                }
            EOF
            % for key, value in module.additionalInputVariables.items():
            ${key} = ${dumps(render_template_string(aws_account, value)) if isinstance(value, str) else dumps(value)}
            % endfor
        }
        """,
        "dedent",
        dumps=json.dumps,
        indent=indent,
        normalized_name=normalized_name,
        workspace=workspace,
        variables=variables,
        provider_variables=provider_variables,
        module=terraform_module,
        provider_snippets=provider_snippets,
    )

    return TerraformWorkspaceCreationCode(value=code)


def get_rules() -> list[Rule]:
    return collect_rules()
