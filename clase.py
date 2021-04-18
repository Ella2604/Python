class Person:
    """
    constructor
    """
    def __init__(self, name = " Pop ", age = "28"):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + "has " + str(self.age)

    def public_methode(self):
        self.__private_methode()

    """
       abstractizare
    """
    @property
    def name_prop(self):
        return self.name

    @name_prop.setter
    def name_prop(self, value):
        self.name = value

    """
       mostenire
    """

class ChildPerson(Person):
        def __init__(self, name="Child Vlad ", age="12"):
            super().__init__(name=name, age=age)

if __name__ == "__main__":
    pers1=Person(name = "vlad ", age = "12 ")
    print(pers1)

    pers2=ChildPerson()
    print(pers2)