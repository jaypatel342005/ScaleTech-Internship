class Employee:

    company_name = "ScaleTech"
    @classmethod
    def change_company_name(cls,company_name):
        cls.company_name = company_name

    @staticmethod
    def is_valid_salary(salary):
        if salary >= 25000:
            return True
        return False

    def __init__(self,name,employee_id,salary):
        self.name = name
        self.employee_id = employee_id
        self.__salary = salary
    
    @property
    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        self.__salary = salary

    def work(self):
        print(self.name,"is working")

    def __str__(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.__salary}"
    
    def __eq__(self,other):
        if self.employee_id == other.employee_id:
            return f"employees are same"
        else:
            return f"employees are different"

class developers(Employee):
    def __init__(self,name,employee_id,salary,programming_language):
        super().__init__(name,employee_id,salary)
        self.programming_language = programming_language
    
    def work(self):
        print(self.name,"is writing code in",self.programming_language)
    
    def __str__(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.__salary}, Programming Language: {self.programming_language}"

class manager(Employee):
    def __init__(self,name,employee_id,salary,team_size):
        super().__init__(name,employee_id,salary)
        self.team_size = team_size

    def work(self):
        print(self.name,"is managing a team of",self.team_size,"members")
    
    def __str__(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.__salary}, Team Size: {self.team_size}"

employees = [Employee("Jay",1,10000),developers("Rahul",2,20000,"Python"),manager("Amit",3,30000,5)]

for employee in employees:
    employee.work()

class LogMixin:
    def Log(self,msg):
        print(f"{self.name} is {msg}")

class EmployeeWithLog(Employee,LogMixin):
    def __init__(self,name,employee_id,salary):
        super().__init__(name,employee_id,salary)

    def work(self):
        self.Log("Working as a employee")

employee1 = EmployeeWithLog("Jay",1,10000)
employee1.work()

employee2 = Employee("Rahul",2,20000)
print(employee1 == employee2)

Employee.change_company_name("ScaleTech.xyz")
print(Employee.company_name)
employee2.change_company_name("ScaleTech")
print(Employee.company_name)
print(employee2.company_name)

print(employee1.is_valid_salary(10000))


    
        
    