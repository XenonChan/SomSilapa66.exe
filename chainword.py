l = int(input())
n = int(input())
word = []

for i in range(n):
    word.append(str(input()))

lastword = word[0]

def checkword(word1, word2):
    count = 0
    for i in range(l):
        if word1[i] != word2[i]:
            if count > 1:
                return False
            count += 1
    return True

for i in word[1:]:
    if checkword(lastword, i):
        lastword = i
    else:
        break
print(lastword)