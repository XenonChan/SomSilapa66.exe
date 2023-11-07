n = int(input())

results = []

for i in range(n, 100):
    if n < 10:
        break
    tens = i // 10
    onece = i % 10
    
    if tens + onece == 10:
        results.append(i)
        

print(" ".join(map(str, results)))