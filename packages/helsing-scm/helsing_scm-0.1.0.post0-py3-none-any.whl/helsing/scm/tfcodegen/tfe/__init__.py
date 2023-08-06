from adjudicator import Rule
from equilibrium import Resource

from . import create_workspace, settings


def get_resources() -> list[type[Resource.Spec]]:
    return [
        *settings.get_resources(),
    ]


def get_rules() -> list[Rule]:
    return [
        *create_workspace.get_rules(),
    ]
