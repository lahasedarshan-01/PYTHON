source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

with open(source, "r") as f1, open(destination, "w") as f2:
    
    for line in f1:
        line = line.strip()
        
        if line.startswith("#") or line == "":
            continue
        
        f2.write(line + "\n")

print("\nSource File Content:")
with open(source, "r") as f:
    print(f.read())

print("\nDestination File Content (without comments):")
with open(destination, "r") as f:
    print(f.read())