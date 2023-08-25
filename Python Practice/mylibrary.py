class Library:
  def __init__(self, n, lst):
    self.n = n
    self.lst = lst
  def books(self):
    print(self.lst)
  def add_books(self, add):
    self.lst.append(add)
  def num_books(self):
    print(len(self.lst))
n = 3
lst = ['a', 'b', 'c']
obj1 = Library(n, lst)
obj1.books()
obj1.num_books()
obj1.add_books('d')
obj1.books()
obj1.num_books()