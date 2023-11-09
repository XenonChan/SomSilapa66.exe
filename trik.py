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


def print_number_pyramid(n):
    current_number = 10
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append(str(current_number))
            current_number += 1
        row_str = ' '.join(row)
        print(row_str)

# ตัวอย่างการเรียกใช้งาน
n = int(input("ป้อนค่า n: "))
print_number_pyramid(n)
