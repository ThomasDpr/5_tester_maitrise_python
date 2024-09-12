# Écrivez votre code ici !

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def afficher_details(self):
        print(f"Nom: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def afficher_details(self):
        super().afficher_details()
        print(f"Salaire: {self.salary}")


employee = Employee("Thomas", 25, 3000)
employee.afficher_details()
