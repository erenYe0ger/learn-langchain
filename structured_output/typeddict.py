from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int


person1: Person = {
    'name': 'elon',
    'age': 50
}

print(person1)