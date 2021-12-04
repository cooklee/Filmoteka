class Person:
    id = 1

    def __init__(self, name, last_name):
        self.id = Person.id
        Person.id += 1
        self.name = name
        self.last_name = last_name


lst = []
for x in range(10):
    lst.append(Person('s', 'sb'))

for person in lst:
    print(person.id)
