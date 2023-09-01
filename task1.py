class person:
    def __init__(self, name, loan, salary):
        self.name = name
        self.salary = salary
        self.loan = loan

    def add_salary(self, amount_salary):
        self.salary += amount_salary

    def add_loan(self, amount_loan):
        self.loan += amount_loan


class employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def add_salary_emp(self, amount_salary):
        self.salary += amount_salary

    def change_position(self, new_position):
        self.position = new_position


# (((Customer)))
customer_1 = person("mohamed", 2000, 3000)
print(f"customer name: {customer_1.name}")
print(f"customer loan: {customer_1.loan}")
print(f"customer salary: {customer_1.salary}")
# add loan,salary--->customer
customer_1.add_loan(2500)
customer_1.add_salary(7000)
print(f"customer new_loan: {customer_1.loan}")
print(f"customer new_salary: {customer_1.salary}")

# (((Eployee)))
employee_1 = employee("ahmed", 7500, "cfo")
print(f"emp salary: {employee_1.name}")
print(f"emp salary: {employee_1.salary}")
print(f"emp salary: {employee_1.position}")
# change salary,position--->Eployee
employee_1.add_salary_emp(1000)
employee_1.change_position("manager")
print(f"emp new_salary: {employee_1.salary}")
print(f"emp new_position: {employee_1.position}")
