s1 = int(input("Enter subject one mark = "))
s2 = int(input("Enter subject two marks= "))
s3 = int(input("Enter subject mark three = "))
total = s1 + s2 + s3
avg = total / 3
print("The total marks out of 300 = ",total)
print("The avergae is = ",avg)
if avg >= 90 and avg <= 100:
    print("A Grade")
elif avg >=70 and avg <= 89:
    print("B Grade")
elif avg >=35 and avg <= 69:
    print("C Grade")
else:
    print("Back to college")