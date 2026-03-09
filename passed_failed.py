vathmoi = [12, 8, 15, 9, 20, 5, 11]
passed = []
failed = []
for i in vathmoi:
    if i > 9:
     passed.append(i)
    else:
        failed.append(i)
print ("Περάσαν οι μαθητές με τους βαθμούς: " + str(passed))
print ("Δεν πέρασαν οι μαθητές με τους βαθμούς: " + str(failed))
