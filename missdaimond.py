text = str(input())

for i in range(-(len(text)-1)//2, (len(text)-1)//2 + 1):
    for j in range(0, abs(i)):
        print(" ")
    for j in range(abs(i), len(text) - abs(i)):
        print(text[j])