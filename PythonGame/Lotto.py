import random


class Hazard:

    @staticmethod
    def lotto() -> None:
        ileliczb = int(input("Podaj ilość typowanych liczb: "))
        maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))

        liczby = []

        i = 0

        while i < ileliczb:
            liczba = random.randint(1, maksliczba)
            if liczby.count(liczba) == 0:
                liczby.append(liczba)
                i = i + 1

        print("Wylosowane liczby:", liczby)

    def loop(self) -> None:
        question = input("""Czy chcesz powtórzyć losowanie? "tak" "lub" "nie" """)
        if question == "tak":
            self.lotto()
        else:
            print("Dziękujemy za udział")

        while question:
            if question == "nie":
                question = True
                quit()
            else:
                self.loop()


hazard = Hazard()
hazard.lotto()
hazard.loop()
