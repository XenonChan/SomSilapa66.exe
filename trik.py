pattern = str(input())

ls = [1, 0, 0]

for i in pattern:
  if i == "A":
    ls[0], ls[1] = ls[1], ls[0]
  elif i == "B":
    ls[1], ls[2] = ls[2], ls[1]
  elif i == "C":
    ls[0], ls[2] = ls[2], ls[0]

for j in range(3):
  if ls[j] == 1:
    print(j + 1)



def is_increasing(number):
    return all(number[i] <= number[i + 1] for i in range(len(number) - 1))

def is_decreasing(number):
    return all(number[i] >= number[i + 1] for i in range(len(number) - 1))

def find_increasing_decreasing_numbers(n):
    numbers = []
    for num in range(100, n + 1):
        num_str = str(num)
        if is_increasing(num_str) or is_decreasing(num_str):
            numbers.append(num_str)
    return numbers

n = int(input("ป้อนค่า n (100-999): "))
if 100 <= n < 1000:
    result = find_increasing_decreasing_numbers(n)
    if result:
        print("ตัวเลขที่เรียงแบบบวกหรือแบบลดลง:", result)
    else:
        print("ไม่พบตัวเลขที่เรียงแบบบวกหรือแบบลดลงในช่วงนี้")
else:
    print("โปรดป้อนค่า n ในช่วง 100-999 เท่านั้น")
