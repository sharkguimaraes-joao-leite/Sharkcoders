#Dunder Methods (double underscore) = Called by Pyhton built-in operators

class book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.auhtor
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, key):
        return key in self.title or key in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return "Not Valid"

book1 = book("Harry Potter", "J.K. Rowling", 223)
book2 = book("The Hobbit", "J.R.R. Tolkien", 310)
book3 = book("Wicked: The untold stories of the witches of Oz", "Gregory Maguire", 560)

print(book3)
print("----------------")
print(book1 == book2)
print("----------------")
print(book3 > book2)
print("----------------")
print(book1 < book2)
print("----------------")
print(book1 + book3)
print("----------------")
print("untold" in book3)
print("----------------")
print(book2["author"])