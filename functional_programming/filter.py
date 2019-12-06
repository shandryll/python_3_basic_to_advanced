people = [
    {'name': 'Pedro', 'age': 11},
    {'name': 'Mariana', 'age': 18},
    {'name': 'Arthur', 'age': 26},
    {'name': 'Rebeca', 'age': 6},
    {'name': 'Tiago', 'age': 19},
    {'name': 'Gabriela', 'age': 17}
]

less = filter(lambda p: p['age'] < 18, people)
print(list(less))
