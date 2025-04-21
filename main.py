def create_students():
    dictionary = [
        {"name": "Petr", "grades": [80, 75, 82, 79, 88]},
        {"name": "Slava", "grades": [84, 74, 81, 76, 86]},
        {"name": "Masha", "grades": [77, 86, 81, 84, 87]},
        {"name": "Alina", "grades": [77, 76, 87, 89, 86]},
        {"name": "Denis", "grades": [76, 76, 74, 78, 70]}
    ]
    return dictionary


def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


def calculate_overall_average(students):
    all_students_grades = []
    for student in students:
        all_students_grades.extend(student["grades"])

    return calculate_average(all_students_grades) if all_students_grades else 0


def print_all_students(students):
    for student in students:
        average_score = calculate_average(student["grades"])
        is_successful = average_score >= 75
        status = "Успешный" if is_successful else "Отстающий"
        print(f"Студент: {student["name"]}\nСредний балл: {average_score:.2f}\nСтатус: {status}\n")


def remove_student_with_lowest_average(students):
    lowest_average = 100
    student_to_remove = None

    for student in students:
        average = calculate_average(student["grades"])
        if average < lowest_average:
            lowest_average = average
            student_to_remove = student

    if student_to_remove:
        students.remove(student_to_remove)

    return students


students = create_students()
print_all_students(students)
overall_average = calculate_overall_average(students)
print(f"Общий средний балл по всем студентам: {overall_average:.2f}\n")

new_student = {"name": "Nina", "grades": [84, 77, 82, 75, 81]}
students.append(new_student)

remove_student_with_lowest_average(students)
print_all_students(students)
overall_average = calculate_overall_average(students)
print(f"Новый средний балл по всем студентам: {overall_average:.2f}\n")