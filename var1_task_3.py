"""
Дан список students с информацией о результатах контрольной
работы по курсу "Алгоритмы и программирование" в 2021 году.
Каждый элемент списка содержит ФИО студента, номер
группы и оценку за контрольную работу. Вам необходимо:
-  Вывести  список  студентов,  писавших  контрольную  в
  порядке  возрастания  полученных
баллов. Должны выводиться ФИО, номер группы и полученная
оценка в заданном порядке через запятую, каждый результат на
отдельной строке. После этого нужно вывести список
студентов, не писавших контрольную.
-  Реализовать  быстрый поиск информации о студенте по
фамилии или отчеству. Должны выводиться ФИО, номер группы
 и полученная оценка в заданном порядке через запятую,
каждый результат на отдельной строке.
"""

# Влад
full_info = []
with open("students.txt", encoding="utf-8") as info_students:
    # open file with information about students
    for student in info_students:  # iterate over the lines of the file
        info = student.strip().split(",")  # all information about students
        name = info[0].split()  # last name, first name, patronymic
        full_info.append([name[0], name[1], name[2], info[1], info[2]])
        # add list element by element: last name, first name, patronymic,
        # group, mark
full_info.sort(key=lambda x: x[4])  # sort by marks
for person in full_info:  # display information line by line
    print(person)

# Realize quick search about a student by last name or patronymic.
# .\Влад
