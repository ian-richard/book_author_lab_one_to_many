import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

# author first_name, last_name, id = None
# book title, genre, publisher, author,  id = None
author1 = Author("Alice", "Sebold")
author2 = Author("Alice", "Sebold")
author3 = Author("Alice", "Sebold")
author4 = Author("Alice", "Sebold")
author5 = Author("Alice", "Sebold")
author6 = Author("Alice", "Sebold")
author7 = Author("Alice", "Sebold")
author_repository.save(author1)
author_repository.save(author2)
author_repository.save(author3)
author_repository.save(author4)
author_repository.save(author5)
author_repository.save(author6)
author_repository.save(author7)
book1 = Book("Lovely bones", "thriller", "Picador", author1)
book2 = Book("Lovely bones", "thriller", "Picador", author1)
book3 = Book("Lovely bones", "thriller", "Picador", author1)
book4 = Book("Lovely bones", "thriller", "Picador", author1)
book5 = Book("Lovely bones", "thriller", "Picador", author1)
book6 = Book("Lovely bones", "thriller", "Picador", author1)
book7 = Book("Lovely bones", "thriller", "Picador", author1)
book_repository.save(book1)
book_repository.save(book2)
book_repository.save(book3)
book_repository.save(book4)
book_repository.save(book5)
book_repository.save(book6)
book_repository.save(book7)
book_repository.save(book7)