class Employee:
    def get_data(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = int(input("Enter salary: "))

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)


class Manager(Employee):
    def get_manager_data(self):
        self.department = input("Enter department: ")


managers = []

for i in range(10):
    print("\nEnter details of Manager", i+1)
    m = Manager()
    m.get_data()
    m.get_manager_data()
    managers.append(m)

print("\nManager Details:")

for m in managers:
    m.display()
    print("Department:", m.department)
    print()