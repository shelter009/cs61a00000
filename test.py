times = []

times_per_player = [[1, 4, 6, 7], [0, 4, 6, 9]]
for i in times_per_player:
    time = []
    for j in range(1,len(i)):
        time.append(i[j]-i[j-1])
    #print(time)
    times.append(time)
print(times)