class Author:
    
    all = []
    
    def __init__(self, name:str) -> None:
        self.name = name
        Author.all.append(self)
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        return Contract(author=self, book=book, date=date, royalties=royalties)
    
    def total_royalties(self):
        total_contracts = self.contracts()
        return sum([c.royalties for c in total_contracts])
    
class Book:
    
    all = []
    
    def __init__(self, title:str) -> None:
        self.title = title
        Book.all.append(self)
        
    def contracts(self):
        return [c for c in Contract.all if c.book == self]
    
    def authors(self):
        return [c.author for c in Contract.all if c.book == self]

class Contract:
    
    all = []
    
    def __init__(self, author:Author, book:Book, date:str, royalties:int) -> None:
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, auth:Author):
        if not isinstance(auth, Author):
            raise Exception()
        else:
            self._author = auth
            
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, bk:Book):
        if not isinstance(bk, Book):
            raise Exception()
        else:
            self._book = bk
            
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, dt:str):
        if not isinstance(dt, str):
            raise Exception()
        else:
            self._date = dt
            
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, ryt:int):
        if not isinstance(ryt, int):
            raise Exception()
        else:
            self._royalties = ryt
            

    @classmethod
    def contracts_by_date(cls, date:str):
        return [c for c in cls.all if c.date == date]