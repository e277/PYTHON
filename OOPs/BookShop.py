# The Bookshop sells a variety of books, by a number of authors. The data kept on a particular book is listed below:
# - ISBN - is a unique 13 digit commercial book identifier.
# - Title - the name of the book.
# - Author - the names of the persons who wrote the book.
# - Genre - the type of book e.g. fiction, children, computer science text.
# - Year of Publication - the year the title was printed.
# - Quantity in Stock - the total number of copies of the title The Bookshop has available.
# - Sale Price - the price at which the title is offered to a customer.

# Write the following accessor functions in python which take a book as input and return the corresponding attribute of a book.
# - get_isbn(book) – returns the isbn of the given book
# - get_title(book) – returns the title of the given book
# - get_authors(book) – returns the list of authors of the given book
# - get_genre(book) – returns the genre of the given book
# - get_year(book) – returns the year the given book was published
# - get_qty(book) – returns the number of copies of the given book
# - get_saleprice(book) – returns the price of the given book

# Write a function co_authors which takes a book as a parameter and returns the list of co_authors if the book is written by multiple authors and returns an empty list if it is single authored. [Hint: make use of the function len to see if the book is authored by multiple persons.]

# >>> co_authors(b1)
# ['Sussman G.', 'Sussman J.']
# >>> co_authors(b2)
# [ ]

# Write a function check_price which takes a bookshop and an isbn and returns the corresponding sale price of the book. If the isbn does not exist print a message “Book not found”. [Use the accessor function to retrieve the isbn of the book in the bookshop]

# >>> check_price(uwi_bookshop, "9780262510875")
# 7340.0
# >>> check_price(uwi_bookshop, "978026251085")
# Book not found

# Write a function books_to_reorder which takes a bookshop and an integer representing reorder level. All books in the bookshop whose quantities are below this reorder are added to a list. For each book that needs to be reordered only the isbn and the titles are added to the list as tuples.

# >>> books_to_reorder(uwi_bookshop,15)
# [('9780262510875', 'Struc. & Interp of Comp. Prog.'), ('9780521644082', 'Haskell School of Expr.')]

# Code:

def makebook(isbn, title, authors, genre, year, qtystck, saleprice):
    """constructor - creates a book"""
    return [isbn, title, authors, genre, year, qtystck, saleprice]
 
def bookshop():
    """constructor- creates a new bookshop"""
    return ("bookshop", [])
 
def add_book(book, bookshop):
    """constructor - adds a book tot eh bookshop"""
    return bookshop[1].append(book)
     
# example books
b1 = ["9780262510875", "Struc. & Interp of Comp. Prog.", ["Abelson H.", "Sussman G.", "Sussman J."], "CS text", 1996,12, 7340.00]
b2 = ["0216874068000", "Algebra & No. Sys", ["Hunter, J."], "Math text", 1985,30, 1040.00]
b3 = ["9780521644082", "Haskell School of Expr.", ["Hudak, P."], "CS text", 2000, 1, 3455.00]
 
# code to create a uwi_bookshop
uwi_bookshop = bookshop()
add_book(b1, uwi_bookshop)
add_book(b2, uwi_bookshop)
add_book(b3, uwi_bookshop)
   
def get_isbn(book): 
    return book[0]
 
def get_title(book): 
    return book[1]
    
def get_authors(book): 
    return book[2]
    
def get_genre(book):
    return book[3]
    
def get_year(book): 
    return book[4]
    
def get_qty(book): 
    return book[5]
    
def get_saleprice(book): 
     return book[6]
 
def check_price(uwi_bookshop, book):
    for x in uwi_bookshop[1]:
        if(book == get_isbn(x)):
            return get_saleprice(x)
    print("Book not found")
 
def co_authors(book):
    if(len(get_authors(book)) > 1):
        mylist = get_authors(book)
        return mylist[1:]
    else:
        return []
 
def books_to_reorder(uwi_bookshop, num):
    lst = []
    for x in uwi_bookshop[1]:
        if(get_qty(x) < num):
            lst.append((get_isbn(x), get_title(x)))
    return lst


def main():
    print("Price:", check_price(uwi_bookshop, "9780262510875"))
    print("Price:", check_price(uwi_bookshop, "978026251085"))
    print("Co Authors:", co_authors(b3))
    print("Co Authors:", co_authors(b2))
    print("Books To Reorder:", books_to_reorder(uwi_bookshop, 15))

if __name__ == "__main__":
    main()
