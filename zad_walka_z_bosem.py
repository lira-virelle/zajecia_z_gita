HP = int(250)
boss = int(40)
tura = int(input("podaj numer tury: "))
tarcza = int(0.25 * boss)
if tura == 1:
    print(f"gracz otrzymał {boss - tarcza} obrażeń po {tura} turze")
elif tura in [21, 31, 41, 51, 61, 71, 81, 91]:
    print(f"gracz otrzymał {boss - tarcza} obrażeń po {tura} turze")
else:
    print(f"gracz otrzymał {boss - tarcza} obrażeń po {tura} turach")
print(f"poziom życia gracza wynosi {HP - (boss - tarcza) * tura} po {tura} turach")