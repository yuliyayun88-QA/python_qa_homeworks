from book import Book

library = [
   Book('название1', 'автор1'),
   Book('название2', 'автор2'),
   Book('название3', 'автор3')
   ]

for book in library:
    print(f'{book.title} - {book.author}')
