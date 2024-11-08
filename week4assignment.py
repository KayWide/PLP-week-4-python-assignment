#create a class named Person
class Person:

    #constructor with name, age, gender as attributes
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    #implement a method called introduce that prints message introducing onesself
    def introduce(self):
        print("My name is", self.name + ".", self.age, "years of age. And I am", self.gender + ".")

#instance of p1
p1 = Person("Njambi", 20, "female")

#call introduce method
p1.introduce()