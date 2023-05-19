import statistics as stat
from typing import Any

groupmates = [
    {
        "name": "Олег",
        "surname": "Гусейнов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Анастасия",
        "surname": "Гольцова",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Владимир",
        "surname": "Зорин",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
{
        "name": "Кирилл",
        "surname": "Колбасов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [3, 3, 5]
    },
    {
        "name": "Кирилл",
        "surname": "Кузнецов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 3, 4]
    },
    {
        "name": "Игорь",
        "surname": "Тулегенов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 4, 5]
    }
]


def filter_by_mark(mark: int, students: list[dict]) -> list[dict]:
    """Функция фильтрации студентов по заданной средней оценке"""
    return list(filter(lambda student: mark < stat.mean(student['marks']), students))


def print_students(students):
    """Функция вывода на экран списка студентов"""
    print('\nИмя'.ljust(15), 'Фамилия'.ljust(10), 'Экзамены'.ljust(30), 'Оценки'.ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10),
              str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))


def validate_mark(inp_mark: str) -> Any:
    """Функция проверки корректности ввода оценки"""
    stripped_mark = inp_mark.strip()
    if stripped_mark.isdigit():
        dig_mark = int(stripped_mark)
        if 2 <= dig_mark <= 5:
            return dig_mark
        else:
            raise ValueError('Значение средней оценки от 2 до 5.')
    else:
        raise TypeError('Оценка должна быть числом.')


if __name__ == '__main__':
    st_mark = validate_mark(input('Введите значение средней оценки: '))
    print_students(filter_by_mark(st_mark, groupmates))





