class Library:
    def __init__(self, booklist, name):
        self.booklist = booklist
        self.name = name
        self.lendrecord = {}

    def displaybooks(self):
        print(f"\nwelcome to {self.name} ")
        # print(f"These are the books we have: {self.booklist}"
        for book in booklist:
            print(book)

    def addbook(self):
        book = input("Enter the name of book you want to add: ").capitalize()
        self.booklist.append(book)
        print("Book added successfully.")

    def lendbook(self):
        try:
            book = input("Enter the book name: ")
            if book not in self.booklist:
                print(f"This book isn't in library. Taken by {self.lendrecord.get(book)}")
            if book in self.booklist:
                name = input("Enter your name: ")
                self.booklist.remove(book)
                self.lendrecord[book] = name
                print("library successfully updated. You can take the book now.")
        except Exception as e:
                print(e)
                print("Enter the valid input!")

    def returnbook(self):
        book = input("Enter the name of book you want to return: ")
        if book in self.lendrecord:
            self.booklist.append(book)
            del self.lendrecord[book]
            print("Library updated successfully.")
        else:
            print("Enter the valid input!")




if __name__ == '__main__':
    booklist = ["book1", "book2", "book3", "book4"]

    lib = Library(booklist, "Deepak library")

    while True:
        lib.displaybooks()
        user = input("press 1 to add book\npress 2 to lend book\npress 3 to return book\npress 0 to quit\n ")
        if user == "1":
            lib.addbook()
        if user == "2":
            lib.lendbook()
        if user == "3":
            lib.returnbook()
        if user == "0":
            break

