hardness = float(input("Enter Hardness: "))
carbon = float(input("Carbon: "))
tensile = float(input("Tensile: "))

c1 = hardness > 50
c2 = carbon < 0.7
c3 = tensile > 5600

if c1 and c2 and c3:
    grade = 10
elif c1 and c2:
    grade = 9
elif c2 and c3:
    grade = 8
elif c1 and c3:
    grade = 7
elif c1 or c2 or c3:
    grade = 6
else:
    grade = 5

print("Grade of Steel: ",grade)
