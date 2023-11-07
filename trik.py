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


def make_diamond_hole(word):
  """
  สร้างรูทรงเพชรจากคำ

  Args:
    word: คำที่ต้องการสร้างรู

  Returns:
    รูทรงเพชรจากคำ
  """

  # ตรวจสอบความยาวของคำ

  if len(word) <= 2:
    return word

  # สร้างรูทรงเพชร

  diamond_hole = []
  for i in range(len(word)):
    if i == 0:
      diamond_hole.append(" " * (len(word) - 1))
      diamond_hole.append(word[i])
    else:
      diamond_hole.append(" " * (len(word) - i - 2))
      diamond_hole.append(word[i])
  for i in range(len(word) - 2, -1, -1):
    if i == 0:
      diamond_hole.append(word[i])
      diamond_hole.append(" " * (len(word) - 1))
    else:
      diamond_hole.append(word[i])
      diamond_hole.append(" " * (len(word) - i - 2))

  return "".join(diamond_hole)


print(make_diamond_hole("BEDROOM"))
