#โจทย์ Sum_11 ปี 58

a, b = map(int, input().split())

results = []

for i in range(a, b + 1):
    ten = i // 10
    onece = i % 10
    
    if ten + onece == 11:
        results.append(i)

if results == []:
    print("ว่างเปล่า")

for result in results:
    print(result)
