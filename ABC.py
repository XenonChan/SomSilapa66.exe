nums = sorted(list(map(int, input().split())))
pos = input()

for i in pos:
    if i.upper() == "A":
        print(nums[0], end=" ")
    elif i.upper() == "B":
        print(nums[1], end=" ")
    elif i.upper() == "C":
        print(nums[2], end=" ")