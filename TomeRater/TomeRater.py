# User Class
class User(object):
    ## Constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    ## Method returning email address
    def get_email(self):
        return self.email

    ## Method updating email address to a new one
    def change_email(self, address):
        self.email = address
        print("The email belonging to {0} has been changed to {1}.".format(self.name, self.email))

    ## String representation for printing object
    def __repr__(self):
        return "User {name}, email: {email}, books read: {book_count}".format(name = self.name, email = self.email, book_count = len(self.books))

    ## Comparison check for same values against other object
    def __eq__(self, other_user):
        # other_user = User(name, email)
        if (self.name == other_user.name) & (self.email == other_user.email):
            self = other_user

    ## Method adding books to dictionary read by User object
    def read_book(self, book, rating = None):
        # self.rating = rating
        # self.book = book
        self.books[book] = rating

    ## Method iterating through rating values and returning the average
    def get_average_rating(self):
        tot_rating = 0
        ratings_count = len(self.books.values())
        for rating in self.books.values():
            if rating:
                tot_rating += rating
        avg_rating = tot_rating / ratings_count
        return avg_rating




# Book Class
class Book(object):
    ## Constructor
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    ## Method returning title of book
    def get_title(self):
        return self.title
    
    ## Method returning ISBN of book
    def get_isbn(self):
        return self.isbn

    ## String representation for printing object
    def __repr__(self):
        return "{title} - {isbn}".format(title = self.title, isbn = self.isbn)

    ## Method setting a new ISBN for the book object
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The book, {0}, had its ISBN updated.".format(self.title))

    ## Method adding a rating to the object's rating instance variable
    def add_rating(self, rating):
        if rating:
            if (rating >= 0) & (rating <= 4):
                self.ratings.append(rating)
            else:
                print("Invalid Rating")
    
    ## Comparison check for same values against other object
    def __eq__(self, other_book):
        if (self.title == other_book.title) & (self.isbn == other_book.isbn):
            self = other_book
    
    ## Method iterating through rating values and returning the average
    def get_average_rating(self):
        tot_rating = 0
        ratings_count = len(self.ratings)
        for rating in self.ratings:
            if rating:
                tot_rating += rating
        avg_rating = tot_rating / ratings_count
        return avg_rating

    ## Return a consistent hash for an instance of a book object
    def __hash__(self):
        return hash((self.title, self.isbn))


## Fiction - Book Subclass
class Fiction(Book):
    ## Constructor
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    ## Method returning author of book
    def get_author(self):
        return self.author

    ## String representation for printing object
    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)


## Non-Fiction - Book Subclass
class Non_Fiction(Book):
    ## Constructor
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    ## Method returning subject of book    
    def get_subject(self):
        return self.subject

    ## Method returning level of book
    def get_level(self):
        return self.level

    ## String representation for printing object
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)




# TomeRater Class
class TomeRater(object):
    ## Constructor
    def __init__(self):
        self.users = {}
        self.books = {}

    ## Method returning new book object created from instance variables
    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    ## Method returning new Fiction object created from instance variables
    def create_novel(self, title, author, isbn):
        novel = Fiction(title, author, isbn)
        return novel

    ## Method returning new Non-Fiction object created from instance variables
    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction = Non_Fiction(title, subject, level, isbn)
        return non_fiction

    ## Method adding book to user
    def add_book_to_user(self, book, email, rating = None):
        if self.users.get(email):
            self.users[email].read_book(book, rating)
            print("Adding rating to book: {0}".format(book))
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {0}!".format(email))

    ## Method adding user
    def add_user(self, name, email, user_books = None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for book in user_books:
                print("Adding: {0}".format(book))
                ## Method using self
                self.add_book_to_user(book, email)

    ## Method printing catalog of books
    def print_catalog(self):
        for book in self.books:
            print(book)

    ## Method printing users
    def print_users(self):
        for user in self.users.values():
            print(user)

    ## Method printing the most read book
    def most_read_book(self):
        max_count = 0
        for book in self.books:
            if self.books[book] > max_count:
                max_count = self.books[book]
                max_book = book
            else:
                continue
        return max_book
        
    ## Method returning highest rated book
    def highest_rated_book(self):
        highest_rating = 0
        for book in self.books:
            if book.get_average_rating():
                    if book.get_average_rating() > highest_rating:
                        highest_rating = book.get_average_rating()
                        highest_book = book
            else:
                continue
        return highest_book

    ## Method returning most positive user
    def most_positive_user(self):
        avg_rating = 0
        for user in self.users:
            if self.users[user].get_average_rating() > avg_rating:
                avg_rating = self.users[user].get_average_rating()
                positive = self.users[user]
            else:
                continue
        return positive