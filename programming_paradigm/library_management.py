class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False


class Library:

    def __init__(self):

        self._list = []

    def add_book(self,title):
        self._list.append(title)

    def check_out_book(self, title):
 
        for book in self._list:
            if book.title == title:
                if not book._is_checked_out:
                    book.check_out()
                    return True
                else:
                    return False
        return False

    def return_book(self, title):

        for book in self._list:
            if book.title == title:
                if book._is_checked_out:
                    book.return_book()
                    return True
                else:
                    return False
        
        return False

    def list_available_books(self):
       
        print("Available books:")
        for book in self._list:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")


