n  = int(input())

if n == 0 and n == 1:
    print("0")
elif n == 2:
    print("1")

sequence = [0, 1]

while len(sequence) < n:
    next_num = sequence[-1] + sequence[-2]
    sequence.append(next_num)

print(sequence[n - 1])