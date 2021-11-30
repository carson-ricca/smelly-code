class Geeks:
    def __init__(self):
        self._age = 0
        self._name = 'Firstname Lastname'

    def get_age(self):
        print("getter method called")
        return self._age

    def set_age(self, a):
        print("setter method called")
        self._age = a

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    age = property(get_age, set_age)
