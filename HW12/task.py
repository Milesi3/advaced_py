# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv

class Subject:
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.scores = []

    def add_grade(self, grade):
        if grade < 2 or grade > 5:
            raise ValueError("Invalid grade")
        self.grades.append(grade)

    def add_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("Invalid score")
        self.scores.append(score)

    def average_score(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)


class Student:
    def __init__(self, first_name, last_name, subjects_csv):
        self.first_name = first_name
        self.last_name = last_name
        self.subjects = self.load_subjects(subjects_csv)

    def load_subjects(self, subjects_csv):
        subjects = []
        with open(subjects_csv, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                subject_name = row[0]
                subject = Subject(subject_name)
                subjects.append(subject)
        return subjects

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, name):
        if not name[0].isupper() or not name.isalpha():
            raise ValueError("Invalid full name")
        self.first_name, self.last_name = name.split(' ', 1)

    def add_grade(self, subject_name, grade):
        subject = self.get_subject(subject_name)
        subject.add_grade(grade)

    def add_score(self, subject_name, score):
        subject = self.get_subject(subject_name)
        subject.add_score(score)

    def get_subject(self, subject_name):
        for subject in self.subjects:
            if subject.name == subject_name:
                return subject
        raise ValueError("Invalid subject name")

    def average_score(self, subject_name):
        subject = self.get_subject(subject_name)
        return subject.average_score()

    def average_score_all_subjects(self):
        total_scores = []
        total_subjects = 0
        for subject in self.subjects:
            total_scores.extend(subject.scores)
            total_subjects += 1
        if not total_scores:
            return 0
        return sum(total_scores) / len(total_scores)


student = Student("John", "Doe", "Data.csv")

student.add_grade("Math", 4)
student.add_score("Math", 85)

average_math_score = student.average_score("Math")
print(f"Average Math score: {average_math_score}")

average_all_subjects_score = student.average_score_all_subjects()
print(f"Average score across all subjects: {average_all_subjects_score}")
