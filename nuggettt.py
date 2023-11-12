n = int(input())

if n <= 5:
    print("No")
else:
    nugget = set()
    for i in range(n // 6 + 1):
        for j in range((n - i * 6) // 9 + 1):
            for k in range((n - i * 6 - j * 9) // 20 + 1):
                nugget.add(i * 6 + j * 9 + k * 20)
    nugget.remove(0)
    nugget_list = sorted(nugget)
    print("\n".join(map(str, nugget_list)))