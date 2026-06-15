#the first student.py class didn't have much of my own written code. This one i tried writing it more without looking, which is pretty awesome.
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
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
        
        print(f'Student: {self.name}')
        print(f'ID: {self.student_id}')

        for item in self.grades:
            print(f'Subject: {item["subject"]} | Score: {item["score"]}')

        print(f'Average: {self.get_average():.1f}')

        highest = self.get_highest()

        print(f'Highest: {highest["subject"]} | Score: {highest["score"]}')

student1 = Student('Johnny', 39)
student1.add_grade('Dutch', 10)
student1.add_grade('English', 8.5)
student1.add_grade('Art', 5.5)
student1.add_grade('Python Programming', 7)

student1.show_report()