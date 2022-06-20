from prosumer.mqtt import ProsumerMqttClient
from prosumer.settings import PROFILE
from prosumer.subsystem.base import SubsystemBase
from prosumer.subsystem import Generation, Load, Storage


class Prosumer(SubsystemBase):
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

    def on_run(self):
        print("running")
