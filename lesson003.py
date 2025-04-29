
class Person:
    def set_details(self):
        self.name = 'John'
        self.age = 20

    def display(self):
        print('I am a person', self)

    def greet(self):
        print('Hello, how are you doing?', self)

p1 = Person()
p2 = Person()

print(hex(id(Person)))

print(type(p1))
print(type(p2))
print(hex(id(p1)))
print(hex(id(p2)))
print(p1)
print(p2)
print('-'*40)

p1.display()
p1.greet()

p2.display()
p2.greet()
print('-'*40)

p1.name = 'Tom'
print(p1.name)
#print(p2.name)

print('-'*40)
p1.set_details()
p2.set_details()
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
print()

p2.name = 'Jack'
p2.age = 30
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)



