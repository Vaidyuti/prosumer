#!/usr/bin/env python

import time
from prosumer.prosumer import Prosumer


def suspend():
    while True:
        time.sleep(100)


if __name__ == "__main__":
    prosumer = Prosumer()
    prosumer.start()
    suspend()
