class Person: # Object Person
    def __init__(self, name, age): # Constructor in python (Default __init__)
        self.name = name
        self.age = age

    def setSchool(self, school): # Instance creation
        self.school = school

    def getSchool(self):
        return self.school

    def random(self):
        print("My name is", self.name)
        print("My age is", self.age)

demo = Person("Ren", 23)
demo.setSchool("Flinders University")
demo2 = Person("Alice", 25)

print(demo.age)
demo.random()
print(demo.getSchool())
demo2.random()



