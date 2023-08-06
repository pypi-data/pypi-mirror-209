class Material:
    def __init__(
        self,
        type: str = "Cauchy",
        prop: dict = {
            "E": 200e3,
            "nu": 0.3,
            "G": 0.0,
            "rho": 7.7e-9,
        },
    ) -> None:
        self.type = type
        self.prop = prop
        for k, v in prop.items():
            setattr(self, k, v)
