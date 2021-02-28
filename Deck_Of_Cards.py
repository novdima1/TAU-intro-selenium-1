print('Dack Of Cards')

class Card(object):
    GB_VAR = 'Global variable'
    def __init__(self, suit, val):
        self.suit = suit
        self. value = val

    def show(self):
        print ("{} of {}".format(self.value, self.suit))

    def print_global_var(self):
        print(Card.GB_VAR)

class Deck(object):
    def __init__(self):
        pass

class Player(object):
    def __init__(self):
        pass


Club_6 = Card('Clubs', 6)

Club_6.show()
Club_6.print_global_var()


class Name():

    def __init__(self, name):
        self.name = name

    def add_name(self, input):
        return input + " Name"

class Sourname(Name):

    def add_name(self, input):
        return input + " Sourname"

class Person(Sourname):
    pass


person1 = Name('Person1')
print(person1.add_name('This is'))
person2 = Sourname('Person2')
print(person2.add_name('This is'))
person3 = Person('Person3')
print(person3.add_name('This is'))