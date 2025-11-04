class Book:
    def __init__(self , title , author , year):
        self.title = title
        self.author = author
        self.year = year

a = Book("Quyonlar Saltanati", "Xudoyberdi To'xtaboyev", 1400)
print(a.title)
print(a.author)
print(a.year)