from pojisteny import Pojisteny
class EvidencniAplikace:
    def __init__(self):
        self.pojisteni = []

    def vytvor_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.pojisteni.append(pojisteny)

    def zobraz_seznam(self):
        for pojisteny in self.pojisteni:
            print(pojisteny)

    def najdi_pojisteneho(self, jmeno, prijmeni):
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                return pojisteny
        return None
