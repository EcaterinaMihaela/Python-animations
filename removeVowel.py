# CAPATINA ECATERINA MIHAELA
# 18.02.2024
# PROGRAMUL ELIMINA VOCALELE DINTR UN SIR DAT DE LA TASTATURA

def citire_sir(nr_cuv):
    string = []
    for i in range(nr_cuv):
        cuvant = input(f"cuvant {i+1}: ")
        string.append(cuvant)
    return string

def afisare_sir(string):
    print("Sirul este:", ' '.join(string))

def eliminare_vocale(string):
    new_string = []
    for cuvant in string:
        new_cuvant = ''.join([char for char in cuvant if char not in 'aeiou'])
        new_string.append(new_cuvant)
    return new_string

def main():
    nr_cuv = int(input("Enter the nr of words: "))
    string = citire_sir(nr_cuv)
    afisare_sir(string)

    # SIRUL FARA VOCALE ESTE:
    new_string = eliminare_vocale(string)
    print("Sirul fara vocale este:", ' '.join(new_string))

if __name__ == "__main__":
    main()

