class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
        if self.capacity < 0:
            raise ValueError("Negative Capacity")

    def __str__(self):
        num = self.size * "🍪"
        return num

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError("Too many cookies")
        else:
            self.size = self.size + n

    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError("Not enough cookies")
        else:
            self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size





