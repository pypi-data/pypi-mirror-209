from typing import Hashable, Mapping, TypeVar

from frozendict import frozendict

__all__ = ["HashableMapping", "FrozenDict"]

K_Hashable = TypeVar("K_Hashable", bound=Hashable)
V_Hashable = TypeVar("V_Hashable", bound=Hashable)


class HashableMapping(Mapping[K_Hashable, V_Hashable], Hashable):
    """
    A hashable mapping.
    """


class FrozenDict(frozendict[K_Hashable, V_Hashable], HashableMapping[K_Hashable, V_Hashable]):
    """
    A concrete implementation of a hashable mapping.
    """

    pass
