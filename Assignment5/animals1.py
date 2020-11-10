

class animal:
    def __init__(self, legs=4, eyes=2, tail=1):
        self.legs=legs
        self.eyes=eyes
        self.tail=tail
     
class wild(animal):
    def habitat(self):
        print("In forests\n")
        
        
class domestic(animal):
    def habitat(self):
        print("Areas habitated by humans\n")
        
        
class Lion(wild):
    def name(self):
        print("Lion:")
    def special(self):
        print("Symbol of Strength and Courage")
    def color(self):
        print("Deep Orange-Brown")
    def food(self):
        print("Meat")


class Tiger(wild):
    def name(self):
        print("Tiger:")
    def special(self):
        print("Indian National Animal")
    def color(self):
        print("orange")
    def food(self):
        print("Meat")
        

class Elephant(wild):
    def name(self):
        print("Elephant:")
    def special(self):
        print("Largest land animals on Earth")
    def color(self):
        print("Gray")
    def food(self):
        print("Grass")
       
       
class Cheetah(wild):
    def name(self):
        print("Cheetah:")
    def special(self):
        print("Fastest Animal on Earth")
    def color(self):
        print("Tan in color with Black Colored Spots")
    def food(self):
        print("Meat")
        

class Baboon(wild):
    def name(self):
        print("Baboon:")
    def special(self):
        print("Distinctive Looking Monkeys")
    def color(self):
        print("Brown")
    def food(self):
        print("Grass, Seeds")
        
   
class Cow(domestic):
    def name(self):
        print("Cow:")
    def special(self):
        print("Gives milk for Humans")
    def color(self):
        print("white,black,brown,etc")
    def food(self):
        print("Grass")
        
        
class Dog(domestic):
    def name(self):
        print("Dog:")
    def special(self):
        print("Symbol of Loyalty")
    def color(self):
        print("White,black,brown,etc")
    def food(self):
        print("Meat,plant based food,etc")
     
        
        
class Goat(domestic):
    def name(self):
        print("Goat:")
    def special(self):
        print("Oldest Domesticated Species of Animal")
    def color(self):
        print("Black,white,etc")
    def food(self):
        print("Grass")
        
        
class Pig(domestic):
    def name(self):
        print("Pig:")
    def special(self):
        print("Great Sense of Smell")
    def color(self):
        print("Pink or Black")
    def food(self):
        print("Distillery Waste")
        

class Donkey(wild):
    def name(self):
        print("Donkey:")
    def special(self):
        print("Load Carriers")
    def color(self):
        print("white")
    def food(self):
        print("Grass")
        
a1=animal(4,2,1)
l1=Lion()
l1.name()
l1.special()
l1.color()
l1.food()
l1.habitat()


t1=Tiger()
t1.name()
t1.special()
t1.color()
t1.food()
t1.habitat()


e1=Elephant()
e1.name()
e1.special()
e1.color()
e1.food()
e1.habitat()


c1=Cheetah()
c1.name()
c1.special()
c1.color()
c1.food()
c1.habitat()


b1=Baboon()
b1.name()
b1.special()
b1.color()
b1.food()
b1.habitat()


c1=Cow()
c1.name()
c1.special()
c1.color()
c1.food()
c1.habitat()


d1=Dog()
d1.name()
d1.special()
d1.color()
d1.food()
d1.habitat()


g1=Goat()
g1.name()
g1.special()
g1.color()
g1.food()
g1.habitat()


p1=Pig()
p1.name()
p1.special()
p1.color()
p1.food()
p1.habitat()
print("No. of legs:",p1.legs)
print("No. of eyes:",p1.eyes)
print("No. of tail:",p1.tail)

