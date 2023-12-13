import random
szam=random.randint(10)
tipp=int(input("Add meg a tipped 1-10 között: "))
if tipp==szam:
    print("eltaláltad")
else:
    print("Nem találtad el")