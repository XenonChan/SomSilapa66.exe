import math
value = []
while True:
    inputs = input()
    if inputs == "":
        break
    try:
        num = int(inputs)
        value.append(num)
    except:
        break

lcm = value[0]
for nums in value:
    lcm = (lcm * nums) // math.gcd(lcm, nums)
print(lcm)