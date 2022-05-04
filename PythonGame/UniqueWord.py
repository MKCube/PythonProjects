zdanie = """How much wood would a woodchuck chuck if a woodchuck could chuck wood?
He would chuck, he would, as much as he could, and chuck as much wood
As a woodchuck would if a woodchuck could chuck wood"""

lista = zdanie.split(',')
unikalne_slowa = []

for slowo in lista:
    slowo_obrobione = slowo.strip("|")
    if slowo not in unikalne_slowa:
        unikalne_slowa.append(slowo)
print(unikalne_slowa)


