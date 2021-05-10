DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

from functools import reduce


def run():
    print('Start')
    data_rows = DATA.copy()
    # Lenguaje python

    python_workers_one = list(filter(lambda x: x.get('language') == 'python', data_rows))
    python_worker = lambda string: string == 'python'
    python_workers_two = [item for item in data_rows if item.get('language') == 'python']
    python_workers_three = [item.get('name') for item in data_rows if python_worker(item.get('language'))]
    print("Lenguaje Python")
    print(python_workers_one)
    print(python_workers_two)
    print(python_workers_three)

    # Edad promedio
    avg_age = round(reduce(lambda a, b: a + b, [item.get('age') for item in data_rows]) / len(data_rows))
    print("Edad promedio")
    print(avg_age)

    # el | es unir un elemento
    # old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    # print(old_people)
    # python 9
    # old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    # print(old_people)


if __name__ == '__main__':
    run()
