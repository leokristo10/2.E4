
def izracunaj_prosjek(lista_brojeva):
    """
    Ova funkcija je "Radnik". Treba primiti listu i vratiti prosjek.
    Implementacija: for petlja za sumu i rukovanje ZeroDivisionError (provjera len()).
    """
    if len(lista_brojeva) == 0:
        return 0

    suma = 0
    for broj in lista_brojeva:
        suma += broj 

    prosjek = suma / len(lista_brojeva)
    return prosjek

    return 0 


lista_mjerenja = []

while True:
    print("\n--- Alat za Prosjek Mjerenja ---")
    print(f"Trenutno u memoriji: {len(lista_mjerenja)} mjerenja")
    print("1. Unesi novo mjerenje (V)")
    print("2. Izračunaj prosjek i obriši mjerenja")
    print("3. Pregledaj sva spremljena mjerenja")
    print("0. Izlaz")
    print("---------------------------------")

    try:
        opcija = int(input("Odaberi opciju: "))
    except ValueError:
        print("Greška: Unos mora biti broj (0-3).")
        continue

    if opcija == 1:
        try:
            vrijednost = float(input("Unesi vrijednost mjerenja (V): "))
            lista_mjerenja.append(vrijednost)
            print(f"Mjerenje {vrijednost} V uspješno dodano.")
        except ValueError:
            print("Greška: Unesena vrijednost mora biti broj.")
    
    elif opcija == 2:
        prosjek = izracunaj_prosjek(lista_mjerenja)
        if len(lista_mjerenja) == 0:
            print("Nema mjerenja za izračun prosjeka.")
        else:
            print(f"Prosjek {len(lista_mjerenja)} mjerenja iznosi: {prosjek:.2f} V")
        lista_mjerenja.clear()
        print("Lista mjerenja je obrisana.")
    
    elif opcija == 3:
        print(f"Spremljena mjerenja: {lista_mjerenja}")
    
    elif opcija == 0:
        print("Izlaz iz programa. Doviđenja!")
        break
    
    else:

        print("Nepostojeća opcija. Pokušaj ponovno.")
