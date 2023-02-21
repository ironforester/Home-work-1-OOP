class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        all_grades = []
        for val in lecturer.grades.values():
            all_grades.extend(val)
        lecturer.average_grade = round(sum(all_grades) / len(all_grades), 2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Нельзя сравнить")
            return
        return self.average_grade < other.average_grade

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершённые курсы: {self.finished_courses}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Нельзя сравнить")
            return
        return self.average_grade < other.average_grade

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade}"

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

        def rate_hw(self, student, course, grade):
            if isinstance(student,
                          Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return "Ошибка"

        all_grades = []
        for val in student.grades.values():
            all_grades.extend(val)
        student.average_grade = round(sum(all_grades) / len(all_grades), 2)
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

first_student = Student("Вася", "Пупкин", "мужик")
first_student.finished_courses += ["Netilogy"]
first_student.courses_in_progress += ["GIT"]
first_student.courses_in_progress += ["Python"]

second_student = Student("Илон", "Маск", "мужик")
second_student.courses_in_progress += ["Python"]
second_student.finished_courses += ["SpaceX"]

first_lecturer = Lecturer("Билли", "Гейтс")
first_lecturer.courses_attached += ["Python"]
first_lecturer.courses_attached += ["GIT"]

second_lecturer = Lecturer("Линус", "Торвальдс")
second_lecturer.courses_attached += ["GIT"]

first_reviewer = Reviewer("Лаврентий", "Берия")
first_reviewer.courses_attached += ["Python"]

second_reviewer = Reviewer("Григорий", "Распутин")
second_reviewer.courses_attached += ["GIT"]
second_reviewer.courses_attached += ["Python"]


student_list = [first_student, second_student]
lecturer_list = [first_lecturer, second_lecturer]

def average_rating_hw(students, courses):
    sum_course_grade = 0
    iterator = 0
    for student in students:
        for key, value in student.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade / iterator, 2)

def average_rating_lesson(lecturers, courses):
    sum_course_grade = 0
    iterator = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade / iterator, 2)

first_student.rate_lect(second_lecturer, "GIT", 10)
first_student.rate_lect(second_lecturer, "GIT", 10)
first_student.rate_lect(first_lecturer, "GIT", 8)
first_student.rate_lect(first_lecturer, "GIT", 8)
first_student.rate_lect(first_lecturer, "Python", 8)
second_student.rate_lect(first_lecturer, "Python", 10)
second_student.rate_lect(first_lecturer, "Python", 8)

second_reviewer.rate_hw(first_student, "Python", 8)
second_reviewer.rate_hw(first_student, "GIT", 9)
second_reviewer.rate_hw(first_student, "GIT", 9)
first_reviewer.rate_hw(first_student, "Python", 8)
first_reviewer.rate_hw(second_student, "Python", 8)
first_reviewer.rate_hw(second_student, "Python", 9)
first_reviewer.rate_hw(second_student, "Python", 9)

print("Список студентов:")
print(f"{first_student}\n")
print(f"{second_student}\n")
print("Список лекторов:")
print(f"{first_lecturer}\n")
print(f"{second_lecturer}\n")
print("Список проверяющих:")
print(f"{first_reviewer}\n")
print(f"{second_reviewer}\n")


print(f"Средняя оценка за дз у {first_student.surname} больше, чем у {second_student.surname} {second_student < first_student}")
print(f"Средняя оценка за лекции у {first_lecturer.surname} меньше, чем у {second_lecturer.surname} {second_lecturer < first_lecturer}\n")



print(f'Средняя оценка студентов за курс GIT: {average_rating_hw(student_list, "GIT")}')
print(f'Средняя оценка студентов за курс Python: {average_rating_hw(student_list, "Python")}')
print(f'Средняя оценка лекторов за курс Python: {average_rating_lesson(lecturer_list, "Python")}')
print(f'Средняя оценка лекторов за курс GIT: {average_rating_lesson(lecturer_list, "GIT")}')