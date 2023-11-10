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


def find_seven_dwarfs(numbers):
  """
  ค้นหาคนแคระทั้งเจ็ดจากตัวเลขทั้งหมด

  Args:
    numbers: ตัวเลขทั้งหมด 9 ตัวเลข

  Returns:
    รายชื่อคนแคระทั้งเจ็ด
  """

  # ตรวจสอบว่าตัวเลขทั้งหมดไม่ซ้ำกัน

  if len(set(numbers)) != 9:
    raise ValueError("ตัวเลขซ้ำกัน")

  # ค้นหาผลรวมที่เป็นไปได้ทั้งหมดจากตัวเลขทั้งหมด

  sums = set()
  for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
      for k in range(j + 1, len(numbers)):
        sum = numbers[i] + numbers[j] + numbers[k]
        sums.add(sum)

  # ค้นหาผลรวมที่เท่ากับ 100

  seven_dwarfs = []
  for sum in sums:
    if sum == 100:
      seven_dwarfs.append(numbers[numbers.index(sum) - 1])
      seven_dwarfs.append(numbers[numbers.index(sum) - 2])
      seven_dwarfs.append(numbers[numbers.index(sum) - 3])
      seven_dwarfs.append(numbers[numbers.index(sum) - 4])
      seven_dwarfs.append(numbers[numbers.index(sum) - 5])
      seven_dwarfs.append(numbers[numbers.index(sum) - 6])
      break

  return seven_dwarfs


if __name__ == "__main__":
  numbers = [7, 8, 10, 13, 15, 19, 20, 23, 25]
  seven_dwarfs = find_seven_dwarfs(numbers)
  print(seven_dwarfs)

