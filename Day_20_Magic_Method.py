# Magic Method--> Dunder method (double underscore) __init__ , __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behaviour of objects

class Book:

    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"   

    def __eq__(self, other):      # to check two objects are equal or not
        return  self.title == other.title and self.author == other.author

    def __lt__(self, other):  # Less than (<)
        return self.num_pages < other.num_pages

    def __gt__(self, other):  # Greater than (>)
            return self.num_pages > other.num_pages
    

book1 = Book("Atomic Habits","KR.Joris",420)
book2 = Book("Atomic Habits","KR.Joris",310)
book3 = Book("The subtle art of Life","J.K.K Haivan",500)
 
print(book1.__str__())  
print(book2.__str__())  
print(book3.__str__())  

print(book1 == book2) # We can check if two objects are equal or not

print(book1<book2)
print(book3>book2)

# Like this there are many other dunder like '__add__' to add 2 page number for example

# '__contains__' --> to search any keywords or words...👍

# '__get__item' --> for indexing 