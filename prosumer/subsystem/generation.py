from datetime import datetime
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
    generation = 0.0
    """The net generation by the system in kW at present."""

    def __init__(self, props: dict[str, any], **kwargs) -> None:
        super().__init__(**props, **kwargs)

    def on_run(self):
        self.generation = self.get_value_for(datetime.now())

    @property
    def export_power(self) -> float:
        return self.generation
