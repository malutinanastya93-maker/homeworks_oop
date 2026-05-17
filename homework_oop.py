class Student:
    """Student class with homework grades and lecture rating."""

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        """Rate a lecturer for a lecture (1-10)."""
        if (isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        """Return average homework grade."""
        all_grades = [g for grades in self.grades.values()
                      for g in grades]
        if not all_grades:
            return 0
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: '
                f'{self._average_grade()}\n'
                f'Курсы в процессе изучения: {in_progress}\n'
                f'Завершенные курсы: {finished}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() < other._average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() <= other._average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() == other._average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() > other._average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() >= other._average_grade()


class Mentor:
    """Parent class for all mentors."""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Lecturer — receives grades from students."""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        """Return average lecture grade."""
        all_grades = [g for grades in self.grades.values()
                      for g in grades]
        if not all_grades:
            return 0
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: '
                f'{self._average_grade()}')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() < other._average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() <= other._average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() == other._average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() > other._average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() >= other._average_grade()


class Reviewer(Mentor):
    """Reviewer — checks homework and grades students."""

    def rate_hw(self, student, course, grade):
        """Rate a student's homework."""
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


def average_student_grade(students, course):
    """Return average homework grade for all students on a course."""
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    if not all_grades:
        return 0
    return round(sum(all_grades) / len(all_grades), 1)


def average_lecturer_grade(lecturers, course):
    """Return average lecture grade for all lecturers on a course."""
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    if not all_grades:
        return 0
    return round(sum(all_grades) / len(all_grades), 1)


# =============================================================
# Task 1: Inheritance
# =============================================================

student_1 = Student('Валерий', 'Гончаров', 'М')
student_2 = Student('Ольга', 'Алёхина', 'Ж')

lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Мария', 'Сидорова')

reviewer_1 = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Анастасия', 'Кузнецова')

# Checking inheritance before assigning courses
print('=== Задание 1: Наследование ===')
print(isinstance(lecturer_1, Mentor))
print(isinstance(reviewer_1, Mentor))
print(lecturer_1.courses_attached)
print(reviewer_1.courses_attached)

# =============================================================
# Task 2: Attributes and class interaction
# =============================================================

# Assigning courses
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2.courses_in_progress += ['Python', 'Java']

lecturer_1.courses_attached += ['Python', 'Git', 'C++']
lecturer_2.courses_attached += ['Python', 'Java']

reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2.courses_attached += ['Python', 'Java']

print('\n=== Задание 2: Взаимодействие ===')

# Reviewers grade students
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 8)

reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Java', 9)

# Students grade lecturers — success cases print None
print(student_1.rate_lecture(lecturer_1, 'Python', 10))
print(student_1.rate_lecture(lecturer_1, 'Git', 8))
print(student_2.rate_lecture(lecturer_1, 'Python', 9))
print(student_2.rate_lecture(lecturer_2, 'Python', 7))
print(student_2.rate_lecture(lecturer_2, 'Java', 10))

# Error: student_1 is not enrolled in C++
print(student_1.rate_lecture(lecturer_1, 'C++', 8))
# Error: student_1 is not enrolled in Java
print(student_1.rate_lecture(lecturer_2, 'Java', 8))
# Error: reviewer is not a Lecturer
print(student_1.rate_lecture(reviewer_1, 'Python', 8))

print(f'\nОценки лектора 1: {lecturer_1.grades}')
print(f'Оценки лектора 2: {lecturer_2.grades}')
print(f'Оценки студента 1: {student_1.grades}')
print(f'Оценки студента 2: {student_2.grades}')

# =============================================================
# Task 3: Polymorphism and magic methods
# =============================================================

print('\n=== Задание 3: __str__ ===')
print(reviewer_1)
print()
print(reviewer_2)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(student_1)
print()
print(student_2)

print('\n=== Сравнение ===')
print(f'Лектор 1 > Лектор 2: {lecturer_1 > lecturer_2}')
print(f'Лектор 1 < Лектор 2: {lecturer_1 < lecturer_2}')
print(f'Лектор 1 == Лектор 2: {lecturer_1 == lecturer_2}')
print(f'Студент 1 > Студент 2: {student_1 > student_2}')
print(f'Студент 1 < Студент 2: {student_1 < student_2}')
print(f'Студент 1 == Студент 2: {student_1 == student_2}')

# =============================================================
# Task 4: Average grade functions
# =============================================================

print('\n=== Задание 4: Средние оценки по курсу ===')
print(f'Средняя ДЗ по Python: '
      f'{average_student_grade([student_1, student_2], "Python")}')
print(f'Средняя ДЗ по Git: '
      f'{average_student_grade([student_1, student_2], "Git")}')
print(f'Средняя лекций по Python: '
      f'{average_lecturer_grade([lecturer_1, lecturer_2], "Python")}')
print(f'Средняя лекций по Java: '
      f'{average_lecturer_grade([lecturer_1, lecturer_2], "Java")}')