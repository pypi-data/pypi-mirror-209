from equilibrium import Resource

from . import v1alpha


def get_resources() -> list[type[Resource.Spec]]:
    return [
        *v1alpha.get_resources(),
    ]
