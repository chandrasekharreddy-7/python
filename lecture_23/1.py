class employee:
    def __init__(self, name, ID, salary):
        self.name = name
        self.ID = ID
        self.salary = salary
    def __str__(self):
        return f"Name : {self.name} \nID : {self.ID} \nsalary = {self.salary}"
    def update_salary(self, new_salary):
        x = self.salary
        self.salary = new_salary
        print(f"your salary is updated from Rs.{x} to Rs.{self.salary}")
class beginner(employee):
    def __init__(self, name, ID, salary, role):
        super().__init__(name, ID, salary)
        self.role = role
    def __str__(self):
        # print(super().__str__())
        # return f"role : {self.role}"
        return super().__str__()+f"\nrole : {self.role}"
class senior_employee(beginner):
    def __init__(self, name, ID, salary, role, leval):
        super().__init__(name, ID, salary, role)
        self.leval = leval
    def __str__(self):
        return super().__str__() + f"\nlevel : {self.leval}"
e1 = senior_employee("chandra sekha reddy", 1, 2500000, "analyst", "senior")
print(e1)
e1.update_salary(300000)
print(e1)