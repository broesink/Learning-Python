class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def __str__(self):
        return f'{self.name} | {self.employee_id} | {self.base_salary}'
    
    def get_annual_salary(self):
        return self.base_salary * 12
    
    def introduce(self):
        print(f'Welcome {self.name}. Your ID is: {self.employee_id} and your annual salary is: {self.get_annual_salary}')

class Manager(Employee):
    def __init__(self, name, employee_id, base_salary, department, team_size):
        super().__init__(name, employee_id, base_salary)
        self.department = department
        self.team_size = team_size

    def get_annual_salary(self):
        return (self.base_salary * 12) * 1.2
    
    def introduce(self):
        print(f'Welcome {self.name}. Your ID is: {self.employee_id} and your annual salary is: {self.get_annual_salary()}. You work at the {self.department} department, and your team size is: {self.team_size}')

    def hold_meeting(self, topic):
        print(f'{self.name} is holding a meeting about {topic}')


employee1 = Employee('James', 34234, 5000)

print(employee1)
print(employee1.get_annual_salary())
employee1.introduce()
