

class Step:
    def __init__(
        self,
        name: str
    ) -> None:
        self.name = name

    def __str__(self) -> str:
        out = "*STEP,"
        out += "*END STEP"
        return out


class StaticStep(Step):
    def __init__(self, name: str) -> None:
        super().__init__(name)
