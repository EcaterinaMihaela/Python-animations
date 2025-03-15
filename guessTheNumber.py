import random

def main():
    print("Guess the number!")
    
    # Generăm un număr aleatoriu între 1 și 10
    interval = random.randint(1, 10)
    
    # Citim numărul de la jucător și verificăm dacă este valid
    try:
        numPlayer = int(input("Introdu un număr între 1 și 10: "))
        if numPlayer < 1 or numPlayer > 10:
            print("Numărul trebuie să fie între 1 și 10.")
            return -1
    except ValueError:
        print("Te rog introdu un număr întreg valid.")
        return -1

    # Verificăm dacă jucătorul a ghicit numărul
    if numPlayer == interval:
        print("You won!")
    else:
        print("You lose! Numărul corect era", interval)

# Pornim jocul
main()
