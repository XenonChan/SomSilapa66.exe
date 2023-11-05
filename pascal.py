m, n = map(int, input().split())

triangle = []

for i in range(11):
    row = []
    for j in range(i + 1):
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    triangle.append(row)

print(triangle[m][n])