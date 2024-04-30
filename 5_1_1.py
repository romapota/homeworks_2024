class Book:
    title = ''
    author = ''
    pages = 0
    year = 0
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
    def __setattr__(self, key, value):
        if ((key == 'title' or key == 'author') and (type(value) != str)) or ((key == 'pages' or key == 'years') and (type(value) != int)):
            raise TypeError("Неверный тип присваиваемых данных")
        else:
            object.__setattr__(self, key, value)


book_1 = Book('Money', 'Irip', 398, 2012)