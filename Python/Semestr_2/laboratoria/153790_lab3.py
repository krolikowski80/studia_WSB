# Zadanie 2.1 Zwierzęta
# Utwórz klasę Animal, która będzie posiadała pola name, age, species oraz weight. Klasa ta powinna posiadać
# również następujące trzy metody:
#   1. Metodę statyczną o nazwie oldest_animal, która będzie przyjmować listę obiektów klasy Animal i zwróci
#       nazwę i wiek najstarszego zwierzęcia na liście.
#   2. Metodę instancji o nazwie is_endangered, która będzie zwracać wartość True lub False, w zależności od
#       tego, czy gatunek zwierzęcia jest zagrożony wyginięciem (przyjmijmy, że tylko gatunek "tiger" jest zagrożony wyginięciem).
#   3. Metodę instancji o nazwie calculate_bmi, która będzie zwracać wartość współczynnika BMI (Body Mass Index)
#       dla danego zwierzęcia na podstawie jego masy ciała i wzrostu. Przyjmij, że wzrost zwierzęcia to 1 metr, a BMI obliczamy ze wzoru: waga / (wzrost2).
#
# Przykład:
# lion = Animal("Simba", 5, "lion", 200)
# tiger = Animal("Shere Khan", 8, "tiger", 150)
# elephant = Animal("Dumbo", 3, "elephant", 400)
# animals = [lion, tiger, elephant]
#
# print(Animal.oldest_animal(animals))
# Shere Khan is the oldest animal at 8 years old
# print(lion.is_endangered())
# False
# print(tiger.is_endangered())
# True
# print(lion.calculate_bmi())
# 200.0
# print(tiger.calculate_bmi())
# 150.0
class Animal:
    def __init__(self, name, age, species, weight):
        self.name = name
        self.age = age
        self.species = species
        self.weight = weight

    @staticmethod
    def oldest_animal(animals):
        # Znajdź najstarsze zwierzę używając funkcji max z kluczem
        oldest = max(animals, key=lambda animal: animal.age)
        return f"{oldest.name} is the oldest animal at {oldest.age} years old"

    def is_endangered(self):
        # Sprawdź, czy gatunek zwierzęcia jest zagrożony wyginięciem
        endangered_species = ["tiger"]
        return self.species.lower() in endangered_species

    def calculate_bmi(self):
        # Oblicz BMI przyjmując wzrost zwierzęcia równy 1 metr
        height = 1  # Zakładamy wzrost zwierzęcia równy 1 metr
        bmi = self.weight / (height**2)
        return bmi


# Przykłady użycia klasy Animal
lion = Animal("Simba", 5, "lion", 200)
tiger = Animal("Shere Khan", 8, "tiger", 150)
elephant = Animal("Dumbo", 3, "elephant", 400)
animals = [lion, tiger, elephant]

# Wywołanie metod i wypisanie wyników
print(
    Animal.oldest_animal(animals)
)  # Wyszukaj i wydrukuj informacje o najstarszym zwierzęciu
print(lion.is_endangered())  # Czy lew jest zagrożony wyginięciem?
print(tiger.is_endangered())  # Czy tygrys jest zagrożony wyginięciem?
print(lion.calculate_bmi())  # Oblicz i wydrukuj BMI dla lwa
print(tiger.calculate_bmi())  # Oblicz i wydrukuj BMI dla tygrysa

# --------------------------------------------------------------------------

# Zad 2.2 Farma
# Utwórz klasę Farm, która będzie posiadała pole instancji animals - listę, w której będą przechowywane wszystkie
# zwierzęta na farmie. Zwierzęta, które będą dodawane do listy muszę być obiektami klasy Animal. Klasa Animal
# może być wykorzystana z poprzedniego zadania. Klasa ta powinna posiadać również następujące trzy metody:
#   1. Metodę instancji add_animal, która będzie dodawać nowe zwierzę na farmę.
#   2. Metodę instancji feed_all, która będzie symulować karmienie wszystkich zwierząt na farmie i zwracać informację
#       o tym jakie jedzenie zostało im podane.
#   3. Metodę klasową create_farm_with_animals, która będzie tworzyć obiekt klasy Farm i dodawać do niego
#       określoną listę zwierząt o zadanej rasie. Metoda ta powinna przyjmować dwa argumenty - listę zwierząt
#       animals_list (bez ich rasy!), które mają zostać dodane na farmę w postaci listy krotek np. [(’Berta’, 5, 400), (’Chirpy’, 2, 430)] oraz rasę dla wszystkich zwierząt species.
# Przykład:
# farm = Farm()
# cow = Animal("Berta", 5, "cow", 400)
# farm.add_animal(cow)
# chicken1 = Animal("Chirpy", 1, "chicken", 1)
# farm.add_animal(chicken1)
# chicken2 = Animal("Cluck", 2, "chicken", 1.2)
# farm.add_animal(chicken2)
# print(farm.animals)
# [Animal(name=’Berta’, age=5, species="cow", weight=400),
# Animal(name=’Chirpy’, age=1, species="chicken", weight=1),
# Animal(name=’Cluck’, age=2, species="chicken", weight=1.2)]
# print(farm.feed_all(’corn’))
# Feeding all animals on farm with corn:
# Berta the cow is being fed.
# Chirpy the chicken is being fed.
# Cluck the chicken is being fed.
# All animals have been fed.
# animals = [
#   ("Berta", 5, 400),
#   ("Chirpy", 1, 430),
#   ("Cluck", 2, 395)
#   ]
# farm1 = Farm.create_farm_with_animals(animals, ’cow’)
# print(farm1.animals)
# [Animal(name=’Berta’, age=5, species="cow", weight=400),
# Animal(name=’Chirpy’, age=1, species="cow", weight=430),
# Animal(name=’Cluck’, age=2, species="cow", weight=395)]


# Definicja klasy Animal
class Animal:
    def __init__(self, name, age, species, weight):
        self.name = name
        self.age = age
        self.species = species
        self.weight = weight


# Definicja klasy FArm
class Farm:
    def __init__(self):
        self.animals = []  # pusta lista, która wypełni się obiektami klasy Animal

    # Dodawanie animala
    def add_animal(self, animal):
        # upewniam się, że dodany zostanie obiekt klasy Animal
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            raise ValueError("Only instances of Animal can be added to the farm.")

    # Karmię wszystkie animalsy
    def feed_all(self, food):
        for animal in self.animals:
            print(f"{animal.name} the {animal.species} is being fed with {food}.")

    @classmethod
    def create_farm_with_animals(cls, animals_list, species):
        new_farm = cls()
        for name, age, weight in animals_list:
            new_farm.add_animal(Animal(name, age, species, weight))
        return new_farm


# Tworzenie instancji farmy
farm = Farm()

# Dodawanie zwierząt do farmy
farm.add_animal(Animal("Berta", 5, "cow", 400))
farm.add_animal(Animal("Chirpy", 1, "chicken", 1))

# Wyświetlenie informacji o zwierzętach na farmie
for animal in farm.animals:
    print(f"{animal.name}, {animal.species}, {animal.age} years old, {animal.weight}kg")

# Karmienie zwierząt
farm.feed_all("corn")

# Tworzenie nowej farmy z listy zwierząt
animals = [("Cluck", 2, 395), ("MooMoo", 1, 430)]
new_farm = Farm.create_farm_with_animals(animals, "cow")
for animal in new_farm.animals:
    print(f"{animal.name}, {animal.species}, {animal.age} years old, {animal.weight}kg")

# # ------------------------------------------------------------------------

# Zad 2.3 Student
# Stwórz klasę Student, która będzie reprezentowała studenta na uczelni. Klasa powinna posiadać następujące pola:
# first_name, last_name, age, gpa (średnia ocen) oraz year. Klasa ta powinna posiadać również następujące trzy
# metody:
#   1. Metodę instancji get_full_name, która będzie zwracać pełne imię i nazwisko studenta
#   2. Metodę instancji is_on_probation, która zwraca wartość logiczną True lub False, w zależności od tego, czy
#       student jest na warunkowym zawieszeniu (w zależności od średniej ocen).
#   3. Metodę statyczną get_average_age, która przyjmuje listę studentów jako argument i zwraca średnią wieku
#       studentów na liście.
#   4. Metodę statyczną get_students_by_year, która przyjmuje listę obiektów klasy Student i zwraca słownik,
#       którego kluczami są lata studiów (od 1 do 5), a wartościami są listy studentów należących do danego roku.
#   5. Metodę statyczną print_students_by_year, która wykorzystuje funkcjonalność metody get_students_by_year
#       i wyświetla studentów według zadanego roku. Tak jak w przypadku metody get_students_by_year przyjmuje
#       ona jako argument listę studentów. UWAGA! Nie kopiować kodu z metody get_students_by_year do
#       metody print_students_by_year!
# Przykład:
# s1 = Student("Jan", "Kowalski", 20, 2, 3.5)
# s2 = Student("Anna", "Nowak", 22, 3, 2.8)
# s3 = Student("Piotr", "Czerwinski", 19, 1, 2.1)
# s4 = Student("Katarzyna", "Wójcik", 21, 4, 4.0)
# print(s1.is_on_probation())
# False
# print(s2.is_on_probation())
# True
# students = [s1, s2, s3, s4]
# print(Student.get_average_age(students))
# 20.5
# students_by_year = Student.get_students_by_year(students)
# print_students_by_year(students)
# 1 rok:
# - Piotr Czerwinski (19 lat, ´srednia ocen: 2.8)
# 2 rok:
# - Jan Kowalski (20 lat, ´srednia ocen: 3.5)
# 3 rok:
# - Anna Nowak (22 lat, ´srednia ocen: 2.8)
# 4 rok:
# - Katarzyna Wójcik (21 lat, ´srednia ocen: 4.0)
# 5 rok:
# Brak


class Student:
    def __init__(self, first_name, last_name, age, year, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.year = year
        self.gpa = gpa

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_on_probation(self):
        return self.gpa < 3.0

    @staticmethod
    def get_average_age(students):
        total_age = sum(student.age for student in students)
        return total_age / len(students)

    @staticmethod
    def get_students_by_year(students):
        year_dict = {}
        for student in students:
            if student.year in year_dict:
                year_dict[student.year].append(student)
            else:
                year_dict[student.year] = [student]
        return year_dict

    @staticmethod
    def print_students_by_year(students):
        students_by_year = Student.get_students_by_year(students)
        for year in range(1, 6):  # Zakładamy, że studia trwają 5 lat
            print(f"{year} rok:")
            if year in students_by_year:
                for student in students_by_year[year]:
                    print(
                        f"- {student.get_full_name()} ({student.age} lat, średnia ocen: {student.gpa})"
                    )
            else:
                print("Brak")


s1 = Student("Jan", "Kowalski", 20, 2, 3.5)
s2 = Student("Anna", "Nowak", 22, 3, 2.8)
s3 = Student("Piotr", "Czerwinski", 19, 1, 2.1)
s4 = Student("Katarzyna", "Wójcik", 21, 4, 4.0)

print(s1.is_on_probation())  # False
print(s2.is_on_probation())  # True

students = [s1, s2, s3, s4]
print(Student.get_average_age(students))  # 20.5

Student.print_students_by_year(students)


# ----------------------------------------------------------

# Zadanie 2.4 Atleta
# Stwórz klasę Athlete, która będzie reprezentować sportowca. Klasa ta powinna mieć pola instancji name, age,
# height, weight, sport, które będą przechowywać odpowiednio: imię i nazwisko, wiek, wzrost, wagę oraz dyscyplinę
# sportową. Dodatkowo, klasa Athlete powinna mieć dwa pola instancji: team oraz country, które będą przechowywać
# odpowiednio nazwę drużyny oraz nazwę kraju, do którego należy dany sportowiec. Wartość tych pól powinna być
# taka sama dla wszystkich instancji tej klasy. Klasa również musi posiadać pole klasy counter, które przy tworzeniu
# obiektu klasy Athlete będzie inkrementowane (zwiększane wraz z pojawianiem się nowych obiektów).
# Klasa powinna mieć metody:
# 1. Metodę instancji get_bmi, która będzie zwracać wartość BMI sportowca na podstawie jego wagi i wzrostu.
# 2. Metodę instancji get_info, która będzie zwracać informacje o sportowcu: imię i nazwisko, wiek, wzrost, wagę,
#   dyscyplinę sportową, nazwę drużyny oraz nazwę kraju.
# 3. Metodę instancji set_team(team), która będzie ustawiać nazwę drużyny
# 4. Metodę instancji set_country(country), która będzie ustawiać nazwę kraju
# 5. Metodę klasy reset_counter, która resetuje pole klasy counter, gdy wywoływany jest destruktor obiektu.
#
# Przykład:
# athlete1 = Athlete("Adam Nowak", 25, 175, 75, "football")
# athlete2 = Athlete("Ewa Kowalska", 30, 180, 68, "tennis")
# athlete1.set_team("Real Madrid")
# athlete2.set_country("Poland")
# print(athlete1.get_bmi())
# 24.49
# print(athlete1.get_info())
# Name: Adam Nowak, Age: 25, Height: 175cm, Weight: 75kg, Sport: football, Team: Real Madrid,
# Country: No country
# print(athlete2.get_info())
# Name: Ewa Kowalska, Age: 30, Height: 180cm, Weight: 68kg, Sport: tennis, Team: No team,
# Country: Poland
# print(Athlete.counter)
# 2
# del athlete1
# print(Athlete.counter)
# 1
# del athlete2
# print(Athlete.counter)


class Athlete:
    team = "No team"  # Wartość domyślna dla wszystkich instancji
    country = "No country"  # Wartość domyślna dla wszystkich instancji
    counter = 0  # Licznik instancji

    def __init__(self, name, age, height, weight, sport):
        self.name = name
        self.age = age
        self.height = height  # w cm
        self.weight = weight  # w kg
        self.sport = sport
        Athlete.counter += 1

    def get_bmi(self):
        height_in_meters = self.height / 100
        return round(self.weight / (height_in_meters**2), 2)

    def get_info(self):
        return (
            f"Name: {self.name}, Age: {self.age}, Height: {self.height}cm, Weight: {self.weight}kg, "
            f"Sport: {self.sport}, Team: {self.team}, Country: {self.country}"
        )

    def set_team(self, team):
        self.team = team

    def set_country(self, country):
        self.country = country

    @classmethod
    def reset_counter(cls):
        cls.counter = 0  # Resetuje licznik instancji

    def __del__(self):
        Athlete.counter -= 1


athlete1 = Athlete("Adam Nowak", 25, 175, 75, "football")
athlete2 = Athlete("Ewa Kowalska", 30, 180, 68, "tennis")
athlete1.set_team("Real Madrid")
athlete2.set_country("Poland")

print(athlete1.get_bmi())  # 24.49
print(athlete1.get_info())
print(athlete2.get_info())
print(Athlete.counter)  # 2

del athlete1
print(Athlete.counter)  # 1

del athlete2
print(Athlete.counter)  # 0
