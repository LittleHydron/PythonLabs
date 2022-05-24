class Transport:
    def __init__(self, license_number: str, mark: str, kind: str = "transport"):
        self.license_number = license_number
        self.mark = mark
        self.kind = kind

    def __str__(self):
        return f"Transport-{self.kind} mark: {self.mark} [{self.license_number}]"
