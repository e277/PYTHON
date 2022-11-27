class Person:
    counter = 0
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f'My name is, {self.name} and age is {self.age}'

# person = Person()
# person.name = 'Ezra'

# person2 = Person('Ezra', 25)
# person2 = Person('Ezra', 25)
# person2 = Person('Ezra', 25)

# print(person2.name, person2.age)
# print(person2.greet())
# print(person2.counter)
# print(id(person2))


# Single Inheritance
class Employee(Person):
    def __init__(self, name=None, age=None, job_title=None):
        super(Employee, self).__init__(name, age)
        self.job_title = job_title

    def greet(self):
        return super(Employee, self).greet() + f" I'm a {self.job_title}" 

# employee = Employee('Keneil', 23, 'Intern')
# print(employee.job_title)
# print(employee.name)
# print(id(employee))