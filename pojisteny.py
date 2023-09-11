class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        while True:
            if self.kontrola_telefonu(telefon):
                self.telefon = telefon
                break
            else:
                telefon = input("Telefonní číslo musí mít přesně 9 číslic. Zadejte znovu: ")

    def kontrola_telefonu(self, telefon):
        return len(telefon) == 9 and telefon.isdigit()

    def __str__(self):
        return f"Jméno: {self.jmeno}, Příjmení: {self.prijmeni}, Věk: {self.vek}, Telefon: {self.telefon}"
