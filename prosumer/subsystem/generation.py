from typing import Optional
from prosumer.subsystem.base import SubsystemBase
from prosumer.subsystem.supports import (
    SupportsExport,
    SupportsRunProfile,
    SupportsTechnologyTag,
)


class Generation(
    SubsystemBase, SupportsRunProfile, SupportsTechnologyTag, SupportsExport
):

    # Static properties
    installed_kw: float
    """
    The installed generating capacity in kW. (i.e. the maximum output power this
    system can yield in ideal conditions).
    """

    # Dynamic properties
    net_generation = 0.0
    """The net generation by the system in kW at present."""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
