from datetime import datetime
from prosumer.subsystem.base import SubsystemBase
from prosumer.subsystem.supports import SupportsImport, SupportsRunProfile


class Load(SupportsRunProfile, SupportsImport, SubsystemBase):

    # Dynamic properties
    consumption = 0.0
    """The net consumption by the system in kW at present."""

    def __init__(self, props: dict[str, any], **kwargs) -> None:
        super().__init__(**props, **kwargs)

    def on_run(self):
        self.consumption = self.get_value_for(datetime.now())

    @property
    def import_power(self) -> float:
        return self.consumption
