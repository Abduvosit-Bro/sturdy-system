students = {}
opened_class = [i for i in range(1, 11)]
closed_class = []

def add_student(name, class1):
    students[name] = class1
    opened_class.remove(class1)
    closed_class.append(class1)

def delete_student(name):
    opened_class.append(students[name])
    closed_class.remove(students[name])
    students.pop(name)

def show_class():
    return closed_class


while True:
    student_name = input('Введите имя и фамилию ученика для регистарции: ')
    student_choice = int(input('1 - Посметреть классы, 2 - Покинуть класс, 3 - Классы  '))
    if student_choice == 1:
        print(opened_class)
        student_class = int(input('Выберите класс: '))
        add_student(student_name, student_class)
        print('Успешно добавлен')
    elif student_choice == 2:
        if student_name in students:
            delete_student(student_name)
        else:
            print('Вас нет в базе')
    elif student_choice == 3:
        print(show_class())
    else:
        print('Не понял')
