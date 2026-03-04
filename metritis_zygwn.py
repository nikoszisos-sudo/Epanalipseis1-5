arithmos = int(input("Δώσε ένα αριθμό: "))
metritis = 0
for i in range(1, arithmos+1, 1):
    if i % 2 == 0:
        metritis += 1
print("βρήκα " + str(metritis) + " ζυγούς αριθμούς")
