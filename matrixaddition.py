m, n = map(int, input().split())

mat1 = []
mat2 = []
results = []

for i in range(m):
  row = list(map(int, input().split()))
  mat1.append(row)

for i in range(m):
  row = list(map(int, input().split()))
  mat2.append(row)

for i in range(m):
  row = []
  for j in range(n):
    row.append(mat1[i][j] + mat2[i][j])
  results.append(row)

for i in range(m):
  print(" ".join(map(str,  results[i])))