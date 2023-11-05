n = int(input())
reverse = 0

count = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

for i in range(10, n + 1):
    if n % 10 == 0:
        pass
    else:
        if n + reverse < 100:
            count += 1

print(count)