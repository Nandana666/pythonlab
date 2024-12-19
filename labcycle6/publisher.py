class Publisher:
	def __init__(self,publisher_id,publisher_name):
		self.publisher_id=publisher_id
		self.publisher_name=publisher_name
	def display(self):
		print(f"publisher Id:{self.publisher_id}")
		print(f"publisher Name:{self.publisher_name}")
class Book(Publisher):
	def __init__(self,publisher_id,publisher_name,title,author):
		super().__init__(publisher_id, publisher_name)
		self.title =title
		self.author =author
	def display(self):
		super().display()
		print(f"Book title:{self.title}")
		print(f"Author:{self.author}")
class Python(Book):
	def __init__(self,publisher_id,publisher_name,title,author,price,no_of_pages):
                super().__init__(publisher_id,publisher_name,title,author)
                self.price=price
                self.no_of_pages=no_of_pages
	def display(self):
                super().display()
                print(f"Book price:{self.price}")
                print(f"no_of_pages:{self.no_of_pages}") 





print("enter the details for the python book")
publisher_id=int(input("enter publisher id:"))
publisher_name=input("enter publisher name:")
title=input("enter the title of the book:")
author=input("enter the author name:")
price=int(input("enter the price:"))
no_of_pages=int(input("enter the number of pages:"))
python_book=Python(publisher_id=publisher_name,publisher_name=publisher_name,title=title,author=author,price=price,no_of_pages=no_of_pages)
print("python book information")
python_book.display()

