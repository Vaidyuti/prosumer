import os

import requests
import yaml

PROFILE_ENDPOINT = os.environ["PROFILE_ENDPOINT"]
PROFILE: dict[str, any] = yaml.safe_load(requests.get(PROFILE_ENDPOINT).text)

VAIDYUTI_SERVER = os.environ.get("VAIDYUTI_SERVER") or "localhost"
VAIDYUTI_MQTT_SERVER = os.environ.get("VAIDYUTI_MQTT_SERVER") or VAIDYUTI_SERVER

# The interval in seconds for publishing the new states.
RUN_INTERVAL = int(os.environ.get("RUN_INTERVAL")) or 5

SUBSYSTEM_REPORTING = ("generation",)
