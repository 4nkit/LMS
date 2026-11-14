from models import Book, Member, Magazine, DVD

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Forbes", 2, 12345)
dvd = DVD("Devdas", 3, 180)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)
print("=========== Library Management System ===========")
print("\n---- Borrowing Library Items ----")
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

print("\n---- Encapsulation ----")
try:
    print(book.__available)
except AttributeError as e:
    print("Encapsulation:", e)

print("Book availability:", book.is_available())

print("\n---- Borrow Limit Check ----")
try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)
except ValueError as e:
    print("Could not borrow:", e)

print("\n---- Returning an item ----")
try:
    fee = alice.return_item(book, days_late=3)
    print("Alice returned the book. Late fee: Rs", fee)
    alice.return_item(magazine)
except ValueError as e:
    print("Return error:", e)

print("\n---- Borrowed Items List ----")
print("Alice's borrowed items:", alice.borrowed_titles())
print("Bob's borrowed items:", bob.borrowed_titles())

print("\n---- Late Fee Check ----")
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

print("\n---- Total Items ----")
print("Total items created:", Book.total_items)
