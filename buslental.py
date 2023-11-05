inputs = list(map(int, input().split()))

bus = [0, 0, 0]
result = []

for i in inputs:
    if bus[0] == 0:
        bus[0] = i
        result.append("A")
    elif bus[1] == 0:
        bus[1] = i
        result.append("B")
    elif bus[2] == 0:
        bus[2] = i
        result.append("C")
    else:
        bus[0] = i
        result.append("A")
    for j in range(3):
        bus[j] -= 1
        if bus[j] < 0:
            bus[j] = 0

print(" ".join(result))

#เสร็จจจจจแล้ววววววววววววววววววววววววววววววววววววววว