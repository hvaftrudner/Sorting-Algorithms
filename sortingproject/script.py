import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
long_bookshelf = utils.load_books('books_large.csv')


for book in bookshelf:
  book['author_lower'] = book['author'].lower()
  book['title_lower'] = book['title'].lower()
  #print(book)
for book in long_bookshelf:
  book['author_lower'] = book['author'].lower()
  book['title_lower'] = book['title'].lower()

  
#print(ord("a"))
#print(ord(" "))
#print(ord("A"))
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()


def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])
    
sort1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort1:
  print(book['title'])
  
sort2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
for book in sort2:
  print(book['author'])
  
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
#print(bookshelf_v2)

#sorts.bubble_sort(long_bookshelf, by_total_length)
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)

#book['author_lower'] = book['author'].lower()
#book['title_lower'] = book['title'].lower()