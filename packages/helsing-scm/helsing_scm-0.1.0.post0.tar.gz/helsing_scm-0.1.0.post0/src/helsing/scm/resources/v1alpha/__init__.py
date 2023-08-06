from equilibrium import Resource

from .AwsAccount import AwsAccount
from .TerraformWorkspace import TerraformWorkspace


def get_resources() -> list[type[Resource.Spec]]:
    return [
        AwsAccount,
        TerraformWorkspace,
    ]
