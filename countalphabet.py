text = str(input())
lenght = len(text)

char_count = {}

for i in text:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

for letter, count in char_count.items():
    print(f"{letter} = {count}")