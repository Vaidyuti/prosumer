from prosumer.subsystem.base import SubsystemBase
from prosumer.subsystem.supports import SupportsExport, SupportsTechnologyTag


class Storage(SubsystemBase, SupportsTechnologyTag, SupportsExport):

    installed_kwh: float
    """
    The installed sotrage capacity in kWh.
    """

    usable_capacity: float

    def __init__(self, props: dict[str, any], **kwargs) -> None:
        super().__init__(**props, **kwargs)

    def on_run(self):
        print("running")
