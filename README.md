# Library Management System

## 1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

LibraryItem is an abstract class because it contains common properties and methods shared by all library items, but we cannot create its object directly. Every child class must have its own implementation of the late_fee() method. If the DVD class does not implement this method, Python will raise a TypeError when we try to create a DVD object.
## 2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

Accessing item.__available directly from outside the class raises an AttributeError because it is a private attribute. Instead, we use the public is_available() method to retrieve the item's availability status while maintaining encapsulation.

## 3. What is the difference between LibraryItem.total_items and self.title?

LibraryItem.total_items is a class attribute shared across all instances of the LibraryItem class and its subclasses, whereas, self.title is an instance attribute, i.e., every individual library item has its own title.