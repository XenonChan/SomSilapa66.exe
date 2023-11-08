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


def is_custom_order(number):
    num_str = str(number)
    for i in range(len(num_str) - 1):
        if (int(num_str[i]) + 1 != int(num_str[i + 1])) and (int(num_str[i]) - 2 != int(num_str[i + 1])):
            return False
    return True

def find_custom_order_numbers(n):
    numbers = []
    for num in range(100, n + 1):
        if is_custom_order(num):
            numbers.append(num)
    return numbers

n = int(input("ป้อนค่า n (100-999): "))
if 100 <= n < 1000:
    result = find_custom_order_numbers(n)
    if result:
        print("ตัวเลขที่เรียงตามรูปแบบที่คุณระบุ:", result)
    else:
        print("ไม่พบตัวเลขที่เรียงตามรูปแบบที่คุณระบุในช่วงนี้")
else:
    print("โปรดป้อนค่า n ในช่วง 100-999 เท่านั้น")
