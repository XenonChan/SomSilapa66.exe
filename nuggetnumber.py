n = int(input())

ways = []
boxsize = [6, 9, 20]

for a in range(n // boxsize[0] + 1):
    for b in range(n // boxsize[1] + 1):
        for c in range(n // boxsize[2] + 1):
            if a * boxsize[0] + b * boxsize[1] + c * boxsize[2] == n:
                ways.append((a, b, c))

if not ways:
    print("NO")
else: 
    for res in ways:
        print(",".join(map(str, res)))