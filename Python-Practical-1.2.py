print("ENTER THE DETAILS BELOW\n")
name = input("Name of vendor: ")
year = int(input("Year of association: "))
contact = input("Contact number: ")
email = input("eMail ID: ")

total_purchase = 0
for i in range(12):
    amount = float(input("Amount: "))
    total_purchase += amount

print("Name: ",name)
print("Year of Association: ",year)
print("Contact Number: ",contact)
print("E-Mail ID: ",email)
print("Total Purchase: ",total_purchase)
