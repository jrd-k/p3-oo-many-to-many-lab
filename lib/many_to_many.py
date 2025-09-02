class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("title must be a string")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Return a list of this book's contracts"""
        return [c for c in Contract.all if c.book is self]

    def authors(self):
        """Return a list of authors for this book"""
        return [c.author for c in self.contracts()]

    def __repr__(self):
        return f"<Book {self.title}>"


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("name must be a string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return a list of this author's contracts"""
        return [c for c in Contract.all if c.author is self]

    def books(self):
        """Return a list of this author's books via contracts"""
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract"""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return the sum of royalties across all contracts"""
        return sum(c.royalties for c in self.contracts())

    def __repr__(self):
        return f"<Author {self.name}>"


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an Author")
        if not isinstance(book, Book):
            raise Exception("book must be a Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts signed on the given date"""
        return [c for c in cls.all if c.date == date]

    def __repr__(self):
        return f"<Contract {self.author.name} - {self.book.title} ({self.date}, {self.royalties}%)>"
