import modul

def data_request():
    dr = int(input(
            "\nМеню:\n" 
            "0 - Добавление нового студента (Поля - имя, фамилия).\n"
            "1 - Добавление предмета (добавляется всем ученикам сразу).\n"
            "2 - Добавление оценки ученику по предмету.\n"
            "3 - Показ списка учеников (имена фамилия).\n"
            "4 - Показ листа оценок конкретного ученика.\n"
            "5 - Генерация фамилий, предметов, оценок и запись их в журнал.\n"
            "6 - Экспор Журнала студентов в файл.\n"
            "7 - Импорт Журнала студентов из файла.\n"
            "8 - Выход из программы.\n"
            "\nВведите номер действия, которое вы хотите совершить: "))
    return dr

def input_student():
    student = input("Введите Фамили и имя студента: ")
    return student

def input_subject():
    subject = input("Предмет: ")
    return subject

def input_grade():
    print(modul.students_name)
    student = input("Введите фамилю: ")
    print(modul.subjecs_list)
    subject = input("Введите предмет: ")
    grade = int(input("Введите оценку: "))
    return student, subject, grade