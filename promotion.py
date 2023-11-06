n, m = map(int, input().split())

m_list = []
remaining = 0

for i in range(m):
    num = int(input())
    m_list.append(num)
    
for j in m_list:
    remaining += j
    
least_table = remaining // n

print(least_table)