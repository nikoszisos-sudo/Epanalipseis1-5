temps = [18, 22, 15, 28, 12, 30, 25]
hot_days = []
for i in temps:
    if i > 24:
     hot_days.append(i)
print ("Οι ζεστές μέρες του μήνα είναι: " + str(hot_days))
print ("Συνολικά είναι: " + str(len(hot_days)) + " μέρες.")
