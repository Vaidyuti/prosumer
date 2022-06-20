from prosumer.subsystem.base import SubsystemBase
from prosumer.subsystem.supports import SupportsRunProfile


class Load(SubsystemBase, SupportsRunProfile):

    # Dynamic properties
    net_consumption = 0.0
    """The net consumption by the system in kW at present."""

    def __init__(self, props: dict[str, any], **kwargs) -> None:
        super().__init__(**props, **kwargs)

    def on_run(self):
        print("running")
