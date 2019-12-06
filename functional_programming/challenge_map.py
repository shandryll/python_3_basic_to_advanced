"""
CHALLENGE:
Using the dictionary below, return the text: '<name> is <age> years old'
people = [
    {'name': 'João', 'age': 31},
    {'name': 'Maria', 'age': 37},
    {'name': 'José', 'age': 26}
]
"""

people = [
    {'name': 'João', 'age': 31},
    {'name': 'Maria', 'age': 37},
    {'name': 'José', 'age': 26}
]

text = map(lambda p: f'{p["name"]} is {p["age"]} years old.', people)
print(list(text))
