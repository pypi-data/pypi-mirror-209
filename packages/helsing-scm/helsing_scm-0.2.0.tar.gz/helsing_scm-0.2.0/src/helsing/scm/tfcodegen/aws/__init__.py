from adjudicator import Rule
from equilibrium import Resource, Service

from . import account_service, create_account, settings


def get_rules() -> list[Rule]:
    return [
        *create_account.get_rules(),
    ]


def get_resources() -> list[type[Resource.Spec]]:
    return [
        *settings.get_resources(),
    ]


def get_services() -> list[Service]:
    return [
        account_service.AwsAccountService(),
    ]
