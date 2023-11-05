def count_numbers(n):
  """
  นับจำนวนตัวเลขน้อยกว่า 100 ที่เท่ากับผลรวมของตัวเลขที่คูณด้วย 10 และบวก 1

  Args:
    n: ตัวเลขเริ่มต้น

  Returns:
    จำนวนตัวเลขที่ตรงเงื่อนไข
  """

  reverse = 0
  count = 0

  for i in range(10, n + 1):
    if i % 10 == 0:
      continue
    else:
      number = i * 10 + reverse
      if number < 100:
        count += 1

  return count


print(count_numbers(100))
