# 2.Fiind dat un dictionar {"a":1,"b":2,"c":3} scrieti o functie care primeste ca parametru cheia si returneaza valoarea

def cheia_valoare(dictionar, cheie):
    try:
        valoare = dictionar[cheie]
        return valoare
    except KeyError:
        return f"Cheia '{cheie}' nu există în dicționar."

dictionar = {"a": 1, "b": 2, "c": 3}

cheie = input("Introduceți cheia: ")
valoare = cheia_valoare(dictionar, cheie)
print(f"Valoarea pentru cheia '{cheie}' este: {valoare}")
