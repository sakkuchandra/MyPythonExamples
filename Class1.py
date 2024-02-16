class Person:
    def __init__(self, name, gender, profession):
        # data members (instance variables)
        self.name = name  
        self.gender = gender
        self.profession = profession

    # Behavior (instance methods)
    def show(self):
        print('Name:', self.name, 'gender:', self.gender, 'Profession:', self.profession)

    # Behavior (instance methods)
    def work(self):
        print(self.name, 'working as a', self.profession)

# create object of a class
jessa = Person('Jessa', 'Female', 'Software Engineer')

# call methods
jessa.show()
jessa.work()

#constructor allows us to initialize the object what we created.
