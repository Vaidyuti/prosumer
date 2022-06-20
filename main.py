#!/usr/bin/env python
import os
import requests
import yaml


def fetch_profile() -> str:
    res = requests.get(os.environ["PROFILE_ENDPOINT"])
    return yaml.safe_load(res.text)


if __name__ == "__main__":
    profile = fetch_profile()
    # Condition Profile
    # Run profile
    pass
