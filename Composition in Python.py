class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def __str__(self):
        return f"Author: {self.name}, Nationality: {self.nationality}"


class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"Book Title: {self.title}, Publication Year: {self.publication_year}, {self.author}"

author1 = Author("J.K. Rowling", "British")
book1 = Book("Harry Potter and the Sorcerer's Stone", author1, 1997)

print(book1)
