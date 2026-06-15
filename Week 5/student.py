class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = []

    def add_grade(self, subject, score):
        self.grades.append({'subject': subject, 'score': score})

    def get_average(self):
        if not self.grades:
            print('No grades yet')
            return
        scores = []

        for item in self.grades:
            scores.append(item['score'])

        average = sum(scores) / len(scores)

        return average
              
    def get_highest(self):
        highest = max(self.grades, key=lambda item: item['score'])
        return highest
        
    def show_report(self):
        if not self.grades:
            print('No grades yet')
            return

        print(f'\nStudent: {self.name}')
        print(f'ID: {self.id}')

        for item in self.grades:
            print(f"Subject: {item['subject']} | Grade: {item['score']}")

        print(f'Average: {self.get_average():.2f}')

        highest = self.get_highest()

        print(f"Highest: {highest['subject']} ({highest['score']})")


student1 = Student("Bauke", 1)
student1.add_grade("Math", 8)
student1.add_grade("English", 7)

print(student1.grades)

student1.show_report()