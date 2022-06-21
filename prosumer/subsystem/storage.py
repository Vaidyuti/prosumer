from prosumer.subsystem.base import SubsystemBase
from prosumer.subsystem.supports import (
    SupportImportAndExport,
    SupportsExport,
    SupportsImport,
    SupportsTechnologyTag,
)


class Storage(SupportsTechnologyTag, SupportImportAndExport, SubsystemBase):

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

    export_power = 0.0
    """
    The net export power from the storage system.
    """

    def __init__(self, props: dict[str, any], **kwargs) -> None:
        super().__init__(**props, **kwargs)

    def on_run(self):
        self.soc = 0.5
        self.export_power = 0.0
