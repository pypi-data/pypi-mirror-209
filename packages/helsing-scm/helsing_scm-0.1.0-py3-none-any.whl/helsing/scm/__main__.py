from logging import basicConfig, getLogger
from pathlib import Path
from subprocess import DEVNULL, run

from adjudicator import Rule, RulesEngine
from equilibrium import Resource, ResourceContext, Service
from rich.logging import RichHandler
from typer import Argument, Typer

from helsing.scm.tfcodegen import generate_terraform_code

logger = getLogger(__name__)
app = Typer(pretty_exceptions_enable=False)


def get_resources() -> list[type[Resource.Spec]]:
    """
    Return the resources to use for generating Terraform code.
    """

    import helsing.scm.resources
    import helsing.scm.tfcodegen

    return [
        *helsing.scm.resources.get_resources(),
        *helsing.scm.tfcodegen.get_resources(),
    ]


def get_services() -> list[Service]:
    """
    Return the services to use for generating Terraform code.
    """

    import helsing.scm.tfcodegen

    return [
        *helsing.scm.tfcodegen.get_services(),
    ]


def get_rules() -> list[Rule]:
    """
    Return the rules to use for generating Terraform code.
    """

    import helsing.scm.tfcodegen

    return [
        *helsing.scm.tfcodegen.get_rules(),
    ]


@app.command()
def main(
    output_dir: Path = Path("generated"),
    manifest_files: list[Path] = Argument(...),
) -> None:
    """
    Secure Cloud Manager generates Terraform code from a declarative specification.
    """

    basicConfig(
        level="INFO",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)],
    )

    context = ResourceContext.create(ResourceContext.InMemoryBackend())
    for resource_type in get_resources():
        logger.info("Register resource type '%s'", resource_type.TYPE)
        context.resource_types.register(resource_type)
    for service_type in get_services():
        logger.info("Register service '%s' for resource type '%s'", service_type.SERVICE_ID, service_type.RESOURCE_TYPE)
        context.services.register(service_type)

    engine = RulesEngine(get_rules(), [context])
    engine.hashsupport.register(Resource, lambda r: hash(r.uri))

    for path in manifest_files:
        logger.info("Loading manifest '%s'", path)
        context.load_manifest(path)

    logger.info("Generating Terraform code in '%s'", output_dir)

    with engine.as_current():
        generate_terraform_code(context=context, directory=output_dir)

    logger.info("Running 'terraform fmt' on directory '%s'", output_dir)
    exit(run(["terraform", "fmt", "--recursive", output_dir], stdout=DEVNULL).returncode)


if __name__ == "__main__":
    app()
