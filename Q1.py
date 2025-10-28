class Book():
    def __init__(self, title, author, isbn, copies) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def borrow(self):
        if self.copies < 0:
            raise Exception as "No copies available"
        self.copies = self.copies - 1
        

    def return_book(self):
        self.copies = self.copies + 1

    
    def __str__(self) -> str:
        return "This is Book class"


class EBook(Book):

    def __init__(self, file_size, title, author, isbn, copies):
        self.__init__(title, author, isbn, copies) = super().title, super().author, super().isbn, super().copies
        self.file_size = file_size

    def __str__(self, file_size):
        self.file_size = file_size
        return super().__str__()

    def borrow(self):
        return super().borrow()

class Library():

    def __init__(self):
        self.__books = []

    def add_book(self, book: Book):
        self.__books = book

    # def find_books_by_author(self, author: str)-> str:
    #     for i in self.__books:

    def __len__(self):
        return len(self.__books)
            
    
