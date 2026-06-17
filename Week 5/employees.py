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
        print(f'Welcome {self.name}. Your ID is: {self.employee_id} and your annual salary is: {self.get_annual_salary()}')

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


class Developer(Employee):
    def __init__(self, name, employee_id, base_salary, programming_language, seniority):
        super().__init__(name, employee_id, base_salary)
        self.programming_language = programming_language
        self.seniority = seniority

    def get_annual_salary(self):
        if self.seniority == 'senior':
            return (self.base_salary * 12) * 1.3
        elif self.seniority == 'mid':
            return (self.base_salary * 12) * 1.15
        elif self.seniority == 'junior':
            return (self.base_salary * 12)
        else:
            raise ValueError('Invalid seniority level')

    def introduce(self):
        print(f'Welcome {self.name}. Your ID is: {self.employee_id} and your annual salary is: {self.get_annual_salary()}. You program in {self.programming_language}, and your employee status is: {self.seniority}')

    def code(self, task):
        print(f'{self.name} is about to finish {task}')

employee1 = Employee('James', 12345, 4000)
employee2 = Employee('Karin', 21345, 3800)
employee3 = Manager('Thomas', 54897, 5000, 'hr', 25)
employee4 = Manager('David', 67890, 6800, 'legal', 12)
employee5 = Developer('Jim', 54734, 5200, 'JavaScript', 'mid')
employee6 = Developer('Ben', 98765, 6000, 'Python', 'junior')

print('=' * 25)
print(employee1)
employee1.introduce()
print('=' * 25)
print(employee2)
employee2.introduce()
print('=' * 25)
print(employee3)
employee3.introduce()
print('=' * 25)
print(employee4)
employee4.introduce()
print('=' * 25)
print(employee5)
employee5.introduce()
print('=' * 25)
print(employee6)
employee6.introduce()
print('=' * 25)