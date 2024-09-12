class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []  # liste des livres disponibles
        self.borrow_books = []  # liste des livres empruntés

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Le livre {book.title} a été ajouté à la bibliothèque.")

    def remove_book(self, book_title: str):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"Le livre {book.title} a été retiré de la bibliothèque.")
                return
        print(f"Le livre {book_title} n'existe pas dans la bibliothèque.")

    def borrow_book(self, book_title: str):
        for book in self.books:
            if book.title == book_title:
                self.borrow_books.append(book)
                self.books.remove(book)
                print(f"Le livre {book.title} a été emprunté de la bibliothèque.")
                return
        print(f"Le livre {book_title} n'est pas disponible dans la bibliothèque.")

    def return_book(self, book_title: str):
        for book in self.borrow_books:
            if book.title == book_title:
                self.books.append(book)
                self.borrow_books.remove(book)
                print(f"Le livre {book.title} a été rendu à la bibliothèque.")
                return
        print(f"Le livre '{book_title}' n'a pas été trouvé parmi les livres empruntés.")

    def available_books(self):
        if self.books:
            print("Livres disponibles dans la bibliothèque :")
            for book in self.books:
                print(f"- {book.title}")
        else:
            print("Aucun livre disponible dans la bibliothèque.")

    def borrowed_books(self):
        if self.borrow_books:
            print("Livres empruntés dans la bibliothèque :")
            for book in self.borrow_books:
                print(f"- {book.title}")
        else:
            print("Aucun livre emprunté dans la bibliothèque.")


# Création de quelques livres
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
book3 = Book("Les Misérables", "Victor Hugo", 1862)

# Création de la bibliothèque
library = Library()

# Ajout des livres à la bibliothèque
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Afficher les livres disponibles
library.available_books()

# Emprunter un livre
library.borrow_book("1984")

# Afficher les livres disponibles après emprunt
library.available_books()

# Afficher les livres empruntés
library.borrowed_books()

# Rendre un livre
library.return_book("1984")

# Afficher les livres disponibles après retour
library.available_books()

# Afficher les livres empruntés après retour
library.borrowed_books()
