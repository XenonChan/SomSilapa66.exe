#โจทย์ palindrome ปี 58

text = str(input())

text = text.lower()
text = ''.join(e for e in text if e.isalnum())

if text == text[::-1]:
    print("Yes")
else:
    print("No")