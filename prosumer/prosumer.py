from functools import reduce
from prosumer.mqtt import ProsumerMqttClient
from prosumer.settings import PROFILE
from prosumer.subsystem.base import SubsystemBase
from prosumer.subsystem import Generation, Load, Storage
from prosumer.subsystem.supports import SupportImportAndExport


class Prosumer(SupportImportAndExport, SubsystemBase):
    def __init__(
        self,
        vp_address: str = PROFILE["vp_address"],
        location: str = PROFILE["location"],
        generations: list = PROFILE["generations"],
        loads: list = PROFILE["loads"],
        storages: list = PROFILE["storages"],
    ) -> None:
        self.vp_address = vp_address
        self.location = location
        self.generations: list[Generation] = list(map(Generation, generations))
        self.loads: list[Load] = list(map(Load, loads))
        self.storages: list[Storage] = list(map(Storage, storages))
        self.mqtt_client = ProsumerMqttClient()
        for sys in (*self.generations, *self.loads, *self.storages):
            sys.start()
        self.mqtt_client.set_state("is_online", True)

    def on_run(self):
        self.mqtt_client.set_states(
            {
                "generation": self.total_generation,
                "load": self.total_load,
                "export": self.export_power,
                "self_consumption": self.self_consumption,
            }
        )

    @property
    def total_generation(self) -> float:
        return sum([sys.export_power for sys in self.generations])

    @property
    def total_load(self) -> float:
        return sum([sys.import_power for sys in self.loads])

    @property
    def net_generation(self) -> float:
        return self.total_generation - self.total_load

    @property
    def self_consumption(self) -> float:
        return min(self.total_load, self.total_generation)

    @property
    def export_power(self) -> float:
        return self.net_generation
