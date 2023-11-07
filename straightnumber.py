n = int(input())
result = []

for i in range(100, n):
    num_str = str(i)
    hundred = i // 100
    tens = (i % 100) // 10
    once = (i % 100) % 10
    
    if hundred != tens != once:
        if all