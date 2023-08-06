import re
from dataclasses import dataclass

from equilibrium import Resource

from helsing.scm import DOMAIN

ACCOUNT_NAME_REGEX = r"^[a-zA-Z0-9][a-zA-Z0-9._-]*$"


@dataclass(frozen=True)
class AwsAccount(Resource.Spec, apiVersion=f"{DOMAIN}/v1alpha1", kind="AwsAccount", namespaced=False):
    """
    Represents an AWS account.
    """

    #: The name of the AWS account in the AWS console.
    accountName: str

    #: The email address associated with the AWS account.
    accountEmail: str

    #: The default region for the AWS account.
    defaultRegion: str

    #: The organizational unit that the AWS account belongs to. This must be a unique name in the
    #: management account. If not specified, the account will be created in the Root OU.
    organizationalUnit: str | None = None

    def __post_init__(self) -> None:
        assert re.match(
            ACCOUNT_NAME_REGEX, self.accountName
        ), f"Invalid account name: {self.accountName!r}, must match {ACCOUNT_NAME_REGEX}"
