from prosumer.subsystem.base import SubsystemBase
from prosumer.subsystem.supports import (
    SupportImportAndExport,
    SupportsExport,
    SupportsImport,
    SupportsTechnologyTag,
)


class Storage(SubsystemBase, SupportsTechnologyTag, SupportImportAndExport):

    # Static Properties
    installed_kwh: float
    """
    The installed sotrage capacity in kWh.
    """

    usable_capacity: float

    # Dynamic Properties
    soc = 0.5
    """
    The State of charge of the storage system.
    """

    def __init__(self, props: dict[str, any], **kwargs) -> None:
        super().__init__(**props, **kwargs)

    def on_run(self):
        self.soc = 0.5

    @property
    def export_power(self) -> float:
        return 0.0  # TODO: update this
