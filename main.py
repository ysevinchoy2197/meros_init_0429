#6-misol
class Shaxs:
    def __init__(self, ism):
        self.ism = ism

    def salom(self):
        print(f"Salom, men {self.ism}")

class Oqituvchi(Shaxs):
    def __init__(self, ism, fan):
        super().__init__(ism)
        self.fan = fan

    def salom(self):
        super().salom()
        print(f"Fan: {self.fan}")


# Test
o = Oqituvchi("Dilnoza", "Matematika")
o.salom()

