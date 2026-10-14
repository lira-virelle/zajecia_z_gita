kawalki_pizza = 8
liczba_osob = int(input("ile osób przyjdzie?:"))
kawalki_na_osobe = int(input("ile kawałków na osobę?: "))
liczba_pizz = (liczba_osob * kawalki_na_osobe + kawalki_pizza - 1) // kawalki_pizza
print(f"potrzebujesz {liczba_pizz} pizzy i {liczba_osob * kawalki_na_osobe} kawałków pizzy")