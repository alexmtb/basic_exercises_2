# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

print('\nЗадание 1:\n')
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

# make dict with name: count of repetitions
students_count = {}
for student in students:
    name = student['first_name']
    if name in students_count:
        students_count[name] += 1
    else:
        students_count[name] = 1

for name, count in students_count.items():
    print(f'{name}: {count}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша

print("\nЗадание 2:\n")
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???
students_count = {}
for student in students:
    name = student['first_name']
    if name in students_count:
        students_count[name] += 1   
    else:
        students_count[name] = 1

name_mode = max(students_count, key=students_count.get)

print(f"Самое частое имя среди учеников: {name_mode}")


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

print("\nЗадание 3:\n")
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


for num, classroom in enumerate(school_students, 1):
    # temp dict for every classroom
    students_count = {}
    for student in classroom:
        name = student['first_name']
        if name in students_count:
            students_count[name] += 1   
        else:
            students_count[name] = 1
    name_mode = max(students_count, key=students_count.get)
    print(f"Самое частое имя в классе № {num}: {name_mode}")



# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

print("\nЗадание 4:\n")

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???
print("\nЗадание 4:\n")
# list comprehension for girls and boys in every class
for i, s_class in enumerate(school, 1):
    girls_count = len([name for name in s_class['students'] if not is_male[name['first_name']]])
    boys_count = len([name for name in s_class['students'] if is_male[name['first_name']]])
    print(f"Класс {s_class['class']}: девочки {girls_count}, мальчики {boys_count}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

print("\nЗадание 5:\n")
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
for s_class in school:
    girls_count = len([name for name in s_class['students'] if not is_male[name['first_name']]])
    boys_count = len([name for name in s_class['students'] if is_male[name['first_name']]])
    if girls_count > boys_count:
        print(f"Больше всего девочек в классе {s_class['class']}")
    elif girls_count < boys_count:
        print(f"Больше всего мальчиков в классе {s_class['class']}")
        

