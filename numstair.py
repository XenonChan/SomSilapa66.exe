n = int(input())
current_value = 10
array = []
for i in range(1, n + 1):
    row = [current_value + j for j in range(i)]
    array.append(row)
    current_value += 10
    
for j in array:
    print(" ".join(map(str, j)))