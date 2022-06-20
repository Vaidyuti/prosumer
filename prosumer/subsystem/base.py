from datetime import datetime
from prosumer.settings import RUN_INTERVAL
from utils.decorators import setInterval


class SubsystemBase:
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
        self.runner: any = None

    def start(self):
        """
        Starts running the subsystem. Does nothing if runner already exists.
        """
        if getattr(self, "runner", None):
            return
        self.started_at = datetime.now()
        self.runner = self.run()

    def stop(self):
        """
        Stops running the subsystem, and clears the runner.
        """
        self.runner.stop()
        self.runner = None

    @setInterval(RUN_INTERVAL)
    def run(self):
        """
        The function that executes every `run_interval` seconds once the
        subsystem is running.
        """
        self.on_run()

    def on_run(self):
        raise NotImplementedError("run")
