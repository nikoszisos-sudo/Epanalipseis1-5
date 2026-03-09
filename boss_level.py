times = [50, 120, 30, 200, 80]
synolo = 0
for i in times:
    synolo += i
if synolo > 400:
    synolo = synolo * 0.9
print("Το συνολικό κόστος των προιοντων είναι: " + str(synolo))
