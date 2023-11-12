n = int(input())
nums = sorted(list(map(int, input().split())))

if n != len(nums):
    print("BruH")

if nums[0] == 0:
    nums[0] == nums[1]
    nums[1] == 0
    
print(nums)