from datetime import datetime
from functools import cached_property

from utils.interpolate import Curves, remap


class SupportsExport:
    export_price: float
    """
    The price at which the energy shall be exported from this system.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def export_power(self) -> float:
        """
        The power at which the energy is being exported at present.
        """
        raise NotImplementedError()


class SupportsImport:
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def import_power(self) -> float:
        """
        The power at which energy is being imported at present.
        """
        raise NotImplementedError()


class SupportImportAndExport(SupportsImport, SupportsExport):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def export_power(self) -> float:
        raise NotImplementedError()

    @property
    def import_power(self) -> float:
        raise -self.export_power


class SupportsTechnologyTag:
    technology = "Unknown"
    """
    The category of technology of this generation system.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class SupportsRunProfile:
    profile: list[float]
    """
    The pre-defined run profile of the system.
    """

    def __init__(self, **kwargs) -> None:
        self.profile = list(map(float, kwargs.pop("profile").split(",")))
        super().__init__(**kwargs)

    @cached_property
    def profile_interval(self):
        """
        Returns the interval in seconds between each point in the predefined
        profile.
        """
        return 24 * 60 * 60 / len(self.profile)

    def get_value_for(self, time: datetime):
        """
        Evaluates the system's generic profile value for the specified time.
        """
        delta = (time - self.start_date).seconds
        #               current time
        # ------------|------*-----|------------>
        #             i      x    i+1
        i = delta // self.profile_interval
        x_minus_i = (delta / self.profile_interval) % 1
        return remap(Curves.sine(x_minus_i), 0, 1, *self.profile[i : i + 2])
