"""
    This code is a class Jar that has many methods that can deposit 
    cookies into the jar withdraw cookies from the Jar, if only the 
    image.pngjar is equal or lesser than the Jar capacity.
"""
class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Wrong capacity input. ")

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("deposit higher than capacity")

        if n + self.size > self.capacity:
            raise ValueError("Higher than capacity")

        self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Trying to remove more than we have in the jar")
        self._size -= n
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

p = Jar()
p.deposit(12)
p.withdraw(3)
print(p)