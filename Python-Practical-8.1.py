with open("input.txt", "r") as f:
    data = f.read()

upper_data = data.upper()

with open("output.txt", "w") as f:
    f.write(upper_data)

print("Data copied in uppercase successfully!")