arithmos = int(input("Δώσε ένα βαθμό απο το 1 ως το 10: "))
while (arithmos <1) or (arithmos > 10):
    arithmos = int(input("Δώσε ένα βαθμό απο το 1 ως το 10: "))
synolo = 0
for i in range(1, arithmos+1, 1):
    synolo = synolo + i
print("Το άθροισμα είναι: " + str(synolo))
