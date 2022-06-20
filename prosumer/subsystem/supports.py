class SupportsExport:
    export_price: float
    """
    The price at which the energy shall be exported from this system.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


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
