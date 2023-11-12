n = int(input("ป้อนจำนวน n (มากกว่า 10 แต่ไม่เกิน 100): "))

if 10 < n <= 100:
    num = 10
    for i in range(1, n - 9):
        for j in range(num, num + i):
            print(j, end=" ")
        num += i
        print()
else:
    print("กรุณาป้อนจำนวน n ที่อยู่ระหว่าง 11 และ 100")