score = int(input())
mid = int(input())
final = int(input())

all_score = score + mid + final

if all_score >= 80:
    print("A")
elif all_score >= 75:
    print("B+")
elif all_score >= 70:
    print("B")
elif all_score >= 65:
    print("C+")
elif all_score >= 60:
    print("C")
elif all_score >= 55:
    print("D+")
elif all_score >= 50:
    print("D")
else:
    print("F")
    