from functools import reduce

people = [
    {'name': 'Pedro', 'age': 11},
    {'name': 'Mariana', 'age': 18},
    {'name': 'Arthur', 'age': 26},
    {'name': 'Rebeca', 'age': 6},
    {'name': 'Tiago', 'age': 19},
    {'name': 'Gabriela', 'age': 17}
]

age_sum = reduce(lambda age, p: age + p['age'], people, 0)
print(age_sum)

less = filter(lambda p: p['age'] < 18, people)
age_sum = reduce(lambda age, p: age + p['age'], less, 0)
print(age_sum)
