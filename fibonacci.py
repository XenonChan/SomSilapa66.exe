a, b = map(int, input().split())

nums = []

for i in range(a, b + 1):
    ten = i // 10
    once = i % 10
    
    if ten + once == 9:
        nums.append(i)
        
if nums == []:
    print("No")
else:
    for results in nums:
        print(results)