from datetime import datetime
from prosumer.subsystem.base import SubsystemBase
from prosumer.subsystem.supports import SupportsImport, SupportsRunProfile


class Load(SupportsRunProfile, SupportsImport, SubsystemBase):

    # Dynamic properties
    import_power = 0.0
    """The net consumption by the system in kW at present."""

    def __init__(self, props: dict[str, any], **kwargs) -> None:
        super().__init__(**props, **kwargs)

    def on_run(self):
        self.import_power = self.get_profile_value(at=datetime.now())
