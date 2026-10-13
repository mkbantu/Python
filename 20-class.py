class employee:
    org_id="004"
    def __init__(self, nom, age, salary, emp_id):
        self.__emp_id =f"{self.org_id}{emp_id}"
        self.name = nom
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Employee ID: {self.__emp_id}"

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
    @classmethod
    def get_org_id(cls):
        return cls.org_id
    @staticmethod
    def get_org_id_static():
        return org_id

emp=employee("John", 30, 50000, "001")
print(emp)
print(emp.name)
print(employee.get_org_id())
