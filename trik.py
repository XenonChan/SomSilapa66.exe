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

n = int(input("ป้อนค่า n (มากกว่า 100 แต่ไม่เกิน 1000): "))

if 100 < n <= 1000:
    # สร้างรายการเริ่มจาก 100 ไปถึง n
    ascending_numbers = list(range(100, n + 1))
    # สร้างรายการเริ่มจาก n ลงมาถึง 100
    descending_numbers = list(range(n, 99, -1))
    
    # แสดงเลขที่เรียงจากน้อยไปมาก
    print("เลขที่เรียงจากน้อยไปมาก:", ascending_numbers)
    # แสดงเลขที่เรียงจากมากไปน้อย
    print("เลขที่เรียงจากมากไปน้อย:", descending_numbers)

    # ลูปและแสดงเลขระหว่าง 100 ถึง n โดยเพิ่มหรือลดทีละ 1
    print("เลขที่เรียงโดยเพิ่มหรือลดทีละ 1:")
    current_number = 100
    while current_number != n:
        print(current_number, end=" ")
        if current_number < n:
            current_number += 1
        else:
            current_number -= 1
    print(n)  # แสดงค่า n ที่ถูกค้นพบ
else:
    print("กรุณาป้อนค่า n ที่อยู่ในช่วง 101 ถึง 1000")

