list_1 = [1, 2, 3]
double = map(lambda x: x * 2, list_1)
print(list(double))

list_2 = [
    {'name': 'João', 'age': 31},
    {'name': 'Maria', 'age': 37},
    {'name': 'José', 'age': 26}
]
only_name = map(lambda n: n['name'], list_2)
print(list(only_name))
only_age = map(lambda a: a['age'], list_2)
print(sum(only_age))
