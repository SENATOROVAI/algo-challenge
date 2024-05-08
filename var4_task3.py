"""Дан список students с информацией 
о результатах контрольной 
работы по курсу "Алгоритмы 
и программирование" в 2021 году.
Каждый элемент списка содержит ФИО 
студента, номер группы и оценку 
за контрольную работу. Вам необходимо
:
﻿﻿Вывести средний балл, набранный 
  студентами по каждой группе.
﻿﻿Реализовать быстрый поиск
  информации о студенте по 
  фамилии или отчеству.
  Должны выводиться ФИО, номер 
  группы и полученная 
  оценка в заданном порядке
  через запятую, калый результ 
  на к зельной строк."""



students = [
    {"full_name": "Иванов Иван Иванович", "group": "101", "grade": 4},
    {"full_name": "Петров Петр Петрович", "group": "101", "grade": 5},
    {"full_name": "Сидоров Алексей Владимирович", "group": "102", "grade": 3},
    {"full_name": "Козлова Ольга Сергеевна", "group": "102", "grade": 4},
    {"full_name": "Смирнова Екатерина Ивановна", "group": "103", "grade": 5},
    {"full_name": "Никитин Никита Никитич", "group": "103", "grade": 4}
]

# Средний балл по каждой группе
group_grades = {}
group_counts = {}
for student in students:
    if student["group"] in group_grades:
        group_grades[student["group"]] += student["grade"]
        group_counts[student["group"]] += 1
    else:
        group_grades[student["group"]] = student["grade"]
        group_counts[student["group"]] = 1

for group, total_grade in group_grades.items():
    avg_grade = total_grade / group_counts[group]
    print(f"Средний балл студентов группы {group}: {avg_grade}")

# Поиск информации о студенте по фамилии или отчеству
def search_student_by_name(name):
    for student in students:
        if name in student["full_name"]:
            print(f"{student['full_name']}, {student['group']}, {student['grade']}")

search_student_by_name("Сидоров")
search_student_by_name("Никитин")
