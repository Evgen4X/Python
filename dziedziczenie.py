class Animal: #klasa nadrzędna
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(self.name)

class Dog(Animal):
    """Klasa Dog dziedziczy wszystko od Animal
Konstruktor __init__ zostaje bez zmian bo go nie nadpisujemy, a funkcja greet zostaje nadpisana"""

    def greet(self):
        print(self.name, "hau hau")

class Fish(Animal):
    """Klasa Fish dziedziczy wszystko od Animal
Fish ma nowy konstruktor__init__ bo go nadpisaliśmy oraz nową funkcję getType, która jest dostępna w klasie Fish, lecz nie ma wpływuna klasę Animal"""
    
    def __init__(self, name, type):
        #wywołujemy kunstruktor klasy nadrzędnej (Animal) aby mieć wszystkie wartości (czyli name), to jest potrzebne tylko jak piszemy nowy konstruktor. W argumentach nie podajemy self
        super().__init__(name)
        self.type = type

    def getType(self):
        #definiujemy nową funkcję dla klasy Fish
        print(self.type)

class TropicalFish(Fish):
    """Klasa TropicalFish dziedziczy od klasy Fish, czyli wówczas ma wszystkie własnośći klasy Animal i Fish"""

    def __init__(self, name):
        #ustawiamy typ na tropical fish
        super().__init__(name, "tropical fish")

#przykłady użycia tego gówna

animal1 = Animal("nwm")
animal1.greet() #output: nwm

dog1 = Dog("Charlie")
dog1.greet() #output: Charlie hau hau
#zostanie wywołana ta funkcja greet, która jest zdefiniowana w klasie Dog, przy czym nadal mamy dostęp do wartości name

fish1 = Fish("Nemo", "Łosoś")
fish1.greet() #output: Nemo
#tu zostanie użyta funkcja greet z klasy Animal ponieważ nie nadpisaliśmy ją w klasie Fish
fish1.getType() #output: Łosoś

fish2 = TropicalFish("Nie-nemo")
fish2.greet() #output: Nie-nemo
#z tej samej przyczyny użyta zostanie funkcja greet klasy Animal
fish2.getType() #output: tropical fish
#ustawiliśmy typ na tropical fish w konstruktorze klasy TropicalFish





