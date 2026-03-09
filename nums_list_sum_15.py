arithmoi = [11, 20, 3, 65]
arithmoi15 = []
metritis = 0
for i in arithmoi:
    metritis += i
print("το άθροισμα των αριθμών της λίστας είναι: " + str(metritis))

for i in arithmoi:
    if i > 15:
     arithmoi15.append(i)
print (arithmoi15)
