n, m = map(int, input().split())
m_list = list(map(int, input().split()))
remaining = 0

if len(m_list) != m:
    print("ใส่ค่าไม่ครบ")
elif len(m_list) > m:
    print("ใส่ค่าเกิน")
    
for j in m_list:
    remaining += j
    
print(remaining // n)
