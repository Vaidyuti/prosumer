import os
from typing import Optional

from paho.mqtt.client import Client

from prosumer import settings


def _on_connect(_client, _userdata, _flags, _rc) -> None:
    print("MQTT Client connected")


def _on_message(_client, _userdata, msg) -> None:
    print(f"MQTT Message Received: {msg}")


def _on_connect_fail(_userdata):
    print("MQTT Connect Failed!")


def _on_disconnect(*args, **kwargs) -> None:
    print(f"MQTT Client Disconnected! {args} {kwargs}")


class ProsumerMqttClient(Client):
    "Custom MQTT client for prosumer."

    def __init__(self):
        self.vp_address = str(settings.PROFILE["vp_address"])
        super().__init__(client_id=self.vp_address)
        self.on_connect = _on_connect
        self.on_disconnect = _on_disconnect
        self.on_message = _on_message
        self.on_connect_fail = _on_connect_fail
        self.will_set(**self._state_to_mqtt_payload(*("is_online", False)))
        self.connect(settings.VAIDYUTI_MQTT_SERVER)
        self.loop_start()

    def _state_to_mqtt_payload(self, state: str, value: any):
        return {
            "topic": f"prosumers/{self.vp_address}/{state}",
            "payload": str(round(value, 3)) if isinstance(value, float) else str(value),
            "retain": True,
        }

    def set_state(
        self, state: str, value: any, parent_state: Optional[str] = None
    ) -> None:
        if state.startswith("$"):
            return
        state = "/".join([parent_state, state]) if parent_state else state
        if isinstance(value, list):
            return self.set_states(
                {str(k): v for k, v in dict(enumerate(value)).items()}, state
            )
        if isinstance(value, dict):
            return self.set_states(states=value, parent_state=state)
        self.publish(**self._state_to_mqtt_payload(state, value))

    def set_states(
        self, states: dict[str, any], parent_state: str | None = None
    ) -> None:
        for item in states.items():
            self.set_state(*item, parent_state=parent_state)
