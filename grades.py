grade = int(input("Δώσε ένα βαθμό απο το 1 ως το 20: "))
while (grade < 1) or (grade > 20):
    grade = int(input("Δώσε ένα βαθμό απο το 1 ως το 20: "))
if grade % 2 == 0:
    print("Ο βαθμός είναι άρτιος")
else:
    print("Ο βαθμός είναι περιττός")
if grade >= 10:
    print("Πέρασες")
else:
    print("κόπηκες")
