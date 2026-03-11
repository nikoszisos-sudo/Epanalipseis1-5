times = [12, 7, 21, 8, 15, 4, 30]
times_artioi = []
times_perittoi = []
synolo = 0
for i in times:
    synolo += i
    if i % 2 == 0:
        times_artioi.append(i)
    else:
        times_perittoi.append(i)
print(times_artioi)
print(times_perittoi)
print(synolo)


