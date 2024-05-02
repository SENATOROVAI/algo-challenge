"""Find info about students."""

full_info = []
with open("students.txt", encoding="utf-8") as info_students:
    for student in info_students:
        info = student.strip().split(",")
        name = info[0].split()
        full_info.append([name[0], name[1], name[2], info[1], info[2]])
full_info.sort(key=lambda x: x[4])
for person in full_info:
    print(person)

# Realize quick search about a student by last name or patronymic.
