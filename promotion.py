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

def make_pearl(word):
  """
  สร้างเพรชจากคำ

  Args:
    word: คำที่ต้องการสร้างเพรช

  Returns:
    เพรชจากคำ
  """

  # แยกคำออกเป็นตัวอักษร
  characters = list(word)

  # กำหนดตัวอักษรเริ่มต้น
  current_character = characters[len(characters) // 2]

  # สร้างเพรช
  pearl = ""
  for i in range(len(characters)):
    # เพิ่มตัวอักษรข้างๆที่ล่ะหนึ่ง
    if i < len(characters) - 1:
      pearl += characters[i]

    # เพิ่มตัวอักษรตรงกลางสุดแบบอยู่ข้างล่าง
    if i > 0:
      pearl += current_character

    # เปลี่ยนตัวอักษรเริ่มต้นเป็นตัวอักษรถัดไป
    current_character = characters[(i + len(characters) // 2) % len(characters)]

  return pearl


print(make_pearl("hello"))
