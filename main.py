from EvidencniAplikace import EvidencniAplikace
if __name__ == "__main__":
    aplikace = EvidencniAplikace()

    while True:
        print("\nVítejte v evidenci pojistných událostí")
        print("1. Vytvořit nového pojištěného")
        print("2. Zobrazit seznam všech pojištěných")
        print("3. Vyhledat pojištěného podle jména a příjmení")
        print("4. Konec")

        volba = input("Vyberte možnost: ")

        if volba == "1":
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            vek = input("Zadejte věk: ")
            telefon = input("Zadejte telefonní číslo: ")
            aplikace.vytvor_pojisteneho(jmeno, prijmeni, vek, telefon)
            print("Pojištěný byl vytvořen.")

        elif volba == "2":
            print("Seznam všech pojištěných:")
            aplikace.zobraz_seznam()

        elif volba == "3":
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            nalezeny_pojisteny = aplikace.najdi_pojisteneho(jmeno, prijmeni)
            if nalezeny_pojisteny:
                print("Nalezený pojištěný:")
                print(nalezeny_pojisteny)
            else:
                print("Pojištěný nebyl nalezen.")

        elif volba == "4":
            print("Konec programu.")


        else:
            print("Neplatná volba. Zkuste to znovu.")

