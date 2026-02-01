name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
basic = float(input("Enter Basic Salary: "))

da = 0.92 * basic
hra = 0.58 * basic
ta = 0.30 * basic
lic = 500

gross_salary = basic + da + hra + ta
net_salary = gross_salary - lic

print("Employee Name: ",name)
print("Employee Id: ",emp_id)
print("Department:",department)
print("Net Salary: ",net_salary)
