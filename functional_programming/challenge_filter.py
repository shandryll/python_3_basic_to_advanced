"""
CHALLENGE:
Using the dictionary below, return the people have most of 6 letters in your name
people = [
    {'name': 'Pedro', 'age': 11},
    {'name': 'Mariana', 'age': 18},
    {'name': 'Arthur', 'age': 26},
    {'name': 'Rebeca', 'age': 6},
    {'name': 'Tiago', 'age': 19},
    {'name': 'Gabriela', 'age': 17}
]
"""

people = [
    {'name': 'Pedro', 'age': 11},
    {'name': 'Mariana', 'age': 18},
    {'name': 'Arthur', 'age': 26},
    {'name': 'Rebeca', 'age': 6},
    {'name': 'Tiago', 'age': 19},
    {'name': 'Gabriela', 'age': 17}
]

most_six_letters = filter(lambda p: len(p['name']) > 6, people)
print(list(most_six_letters))
