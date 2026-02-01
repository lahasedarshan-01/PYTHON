v = float(input("Enter Voltage: "))
r = float(input("Enter Resistance: "))

i = v / r

print(i)

if i < 0.5:
    print("Low current")
elif i <= 2:
    print("Normal current")
else:
    print("High current")
