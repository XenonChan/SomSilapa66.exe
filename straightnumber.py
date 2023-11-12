n = int(input())
result = []

for i in range(100, n):
    num_str = str(i)
    hundred = i // 100
    tens = (i % 100) // 10
    once = (i % 100) % 10
    
    if hundred != tens != once:
        if all(int(num_str[i])  <= int(num_str[i + 1]) for i in range(len(num_str) - 1)):
            result.append(i)
        elif all(int(num_str[i])  >= int(num_str[i + 1]) for i in range(len(num_str) - 1)):
            result.append(i)
print(result)