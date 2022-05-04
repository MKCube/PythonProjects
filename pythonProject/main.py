
class Animal():

    def __init__(self, type, legs, size):
        self.type = type
        self.legs = legs
        self.size = size

    def howAreYou(self):
        print(f"I'am: {self.type} I have: {self.legs} legs, and I'am: {self.size}")

def main():
    Dog = Animal("Dog", 4, "Medium")
    Lion = Animal("Lion", 4, "Big")
    TRex = Animal("TRex", 2, "Very Big")
    Mouse = Animal("Mouse", 4, "Small")

    Dog.howAreYou()
    Lion.howAreYou()
    TRex.howAreYou()
    Mouse.howAreYou()

if __name__ == "__main__":
    main()


print("Write your name:")
x = input()

print("Your name is:" + x)


def number_to_string(num) -> None:
    try:
        return str(num)
    except:
        return None

 def check(seq, elem):
        for i in seq:
            if i == elem:
                return True
        return False



import figury
wybor = input("""Jaką figurę wybierasz?:
1. Kwadrat
2. Prostokąt
3. Koło
4. Trójkąt
5. Trapez
""")
if (wybor =='1'):
    a = float(input("Podaj bok kwadratu: "))
    print("Pole kwadratu to: ", figury.pole_kwadratu(a))

elif (wybor == '2'):
    a = float(input("Podaj pierwszy bok prostokąta: "))
    b = float(input("Podaj drugi bok prostokąta: "))
    print("Pole prostokąta to:", figury.pole_prostokata(a, b))

elif (wybor == '3'):
    r = float(input("Podaj średnicę: "))
    print("Pole koła to: ", figury.pole_kola(r))

elif (wybor == '4'):
    a = float(input("Podaj pierwszy podstawę trójkąta: "))
    h = float(input("Podaj drugi wysokość trójkąta: "))
    print("Pole prostokąta to:", figury.pole_trojkata(a, h))

elif (wybor == '5'):
    a = float(input("Podaj pierwszy bok trapezu: "))
    b = float(input("Podaj drugi bok trapezu: "))
    h = float(input("Podaj wysokość trapezu: "))
    print("Pole prostokąta to:", figury.pole_trapezu(a, b, h))
else:
    print("Nie wybrano odpowiedniej opcji")


# każde działanie daje ten sam efekt, ale ma różną prędkość działania

def sumuj_do(liczba): 
    suma = 0

    for liczba in range(1,liczba + 1):
        suma = suma + liczba

        return  suma

def sumuj_do2(liczba):
    return sum ([liczba for liczba in range (1,liczba + 1)])

def sumuj_do3(liczba):
    return sum ({liczba for liczba in range (1,liczba + 1)})

def sumuj_do4(liczba):
    return sum ((liczba for liczba in range (1,liczba + 1)))

def sumuj_do5(liczba):
    return (1 +liczba) / 2 * liczba

print(sumuj_do(6))
print(sumuj_do2(6))
print(sumuj_do3(6))
print(sumuj_do4(6))
print(sumuj_do5(6))

