students = [
    ["Иванов Иван Иванович", "Группа 1", 85],
    ["Петров Петр Петрович", "Группа 2", 70],
    ["Сидоров Сидор Сидорович", "Группа 1", 90],
    ["Кузнецова Екатерина Павловна", "Группа 3", 95],
    ["Смирнова Анна Ивановна", "Группа 2", 80]
]

# Запрос порогового значения у пользователя
threshold = int(input("Введите пороговое значение: "))

print("Студенты, набравшие баллов больше", threshold)
for student in students:
    if student[2] > threshold:
        print("{}, {}, {}".format(student[2], student[0], student[1]))

# Реализация поиска информации о студенте по имени или отчеству
search_name = input("Введите имя или отчество студента: ")

for student in students:
    if search_name in student[0]:
        print("{}, {}, {}".format(student[0], student[1], student[2]))
