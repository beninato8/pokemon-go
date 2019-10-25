stats = {}

for a in range(16):
    for d in range(16):
        for s in range(16):
            iv = round(sum((a,d,s))*100/45)
            if iv in stats:
                stats[iv] += 1
            else:
                stats[iv] = 1

print(stats)
