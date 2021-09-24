class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        """
        Make a possibility to rate Lecturer's work
        """
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in \
                lecturer.courses_attached and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_avg_grade(self):
        avg_gr = 0
        for course in self.grades:
            avg_gr += sum(self.grades[course]) / len(self.grades[course])
        return avg_gr

    def __lt__(self, other):
        if not isinstance(other, Student):
            return f'Не студент!'
        return self.get_avg_grade() < other.get_avg_grade()

    def __str__(self):
        name_surname = f'Имя: {self.name}\n' \
                       f'Фамилия: {self.surname}\n' \
                       f'Средняя оценка за д/з: ' \
                       f'{round(self.get_avg_grade(), 2)}\n' \
                       f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                       f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return name_surname


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """
        Make a possibility to rate Stident's homework
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress \
                and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name_surname = f'Имя: {self.name}\n' \
                       f'Фамилия: {self.surname}'
        return name_surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_avg_grade(self):
        average_grade = 0
        for course in self.grades:
            average_grade += sum(self.grades[course]) / len(self.grades[course])
        return average_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return f'Не лектор!'
        return self.get_avg_grade() < other.get_avg_grade()

    def __str__(self):
        name_surname = f'Имя: {self.name}\n' \
                       f'Фамилия: {self.surname}\n' \
                       f'Средняя оценка за лекции: ' \
                       f'{round(self.get_avg_grade(), 1)}'
        return name_surname

# Заполняем экземпляры и проводим оценки
# 1 студент
student1 = Student('Al', 'Ig', 'male')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['JavaScript']
student1.courses_in_progress += ['Ruby']
student1.finished_courses += ['Git']
# 2 студент
student2 = Student('Tom', 'Bombadil', 'male')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['JavaScript']
student2.courses_in_progress += ['Ruby']
student2.finished_courses += ['Git']
# 1 лектор
lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Ruby']
# 2 лектор
lecturer2 = Lecturer('Qwe', 'Rty')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['Ruby']
# Проверяющий
reviewer = Reviewer('Alex', 'Ign')
reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['Ruby']

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 7)
student1.rate_lecturer(lecturer1, 'Python', 8)
student1.rate_lecturer(lecturer1, 'Ruby', 7)
student1.rate_lecturer(lecturer1, 'Ruby', 10)

student1.rate_lecturer(lecturer2, 'Python', 10)
student1.rate_lecturer(lecturer2, 'Python', 10)
student1.rate_lecturer(lecturer2, 'Python', 10)
student1.rate_lecturer(lecturer2, 'Ruby', 8)
student1.rate_lecturer(lecturer2, 'Ruby', 9)

reviewer.rate_hw(student1, 'Python', 10)
reviewer.rate_hw(student1, 'Python', 9)
reviewer.rate_hw(student1, 'Python', 8)
reviewer.rate_hw(student1, 'Ruby', 9)
reviewer.rate_hw(student1, 'Ruby', 10)

reviewer.rate_hw(student2, 'Python', 7)
reviewer.rate_hw(student2, 'Python', 8)
reviewer.rate_hw(student2, 'Python', 7)
reviewer.rate_hw(student2, 'Ruby', 5)
reviewer.rate_hw(student2, 'Ruby', 7)

# 4 часть ДЗ

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]


def students_avg_grades(students, course):
    counter = 0
    sum_grade = 0
    for student in students:
        if course in student.grades:
            counter += len(student.grades[course])
            sum_grade += sum(student.grades[course])
        else:
            return f'Нет такого курса, либо нет оценок'
    return round((sum_grade / counter), 2)


def lecturers_avg_grades(lecturers, course):
    counter = 0
    sum_grade = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            counter += len(lecturer.grades[course])
            sum_grade += sum(lecturer.grades[course])
        else:
            return f'Нет такого курса, либо нет оценок'
    return round((sum_grade / counter), 2)


sag = students_avg_grades(students_list, 'Python')
print(sag)

lag = lecturers_avg_grades(lecturers_list, 'Ruby')
print(lag)

# print(lecturer.grades)
# print(lecturer1)
# print(lecturer2)
# m = max(lecturer1, lecturer2)
# m = max(student1, student2)
# print(m)
# print(reviewer)
# print(reviewer.courses_attached)
# print(student1)
# print(student2)
# print(lecturer)
