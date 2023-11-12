x = int(input())
score = []
sumn = 0
mx = 0

for i in range(x):
    a, b = [int(e) for e in input().split()]
    score.append(b - (2 * a))

score.sort(reverse=True)

for k in range(x):
    sumn += score[k]
    n = sumn - (x - k - 1) ** 2
    mx = max(mx, n)

print(mx)