#!/usr/bin/env python3

class Person(object):
    def __init__(self, name):
        self.name = name
    def get_details(self):
        return self.name
    

class Student(Person):   
    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
        
    def get_details(self):
        return'{} studies {}, and is in {}'.format(self.name, self.branch, self.year)


        
class Teacher(Person):    
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers
    def get_details(self):
        return '{} teaches {}'.format(self.name, ','.join(self.papers))

person1 = Person('skdjf')           
studies1 = Student('ljlfj','dkf',1234)
teacher1 = Teacher('dkfjl',['C', 'C++'])

print(person1.get_details())
print(studies1.get_details())
print(teacher1.get_details())
