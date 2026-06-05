class DynamicArray:
    values: List[int]
    size: int
    capacity: int

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise Exception()

        self.values = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        if i < 0 or i > self.capacity - 1:
            raise Exception()

        return self.values[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i > self.capacity - 1:
            raise Exception()

        self.values[i] = n
        self.size = i if i > self.size - 1 else self.size

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.values[self.capacity - 1] = n
        self.size = self.capacity

    def popback(self) -> int:
        result = self.values[self.capacity - 1]
        self.values[self.capacity - 1] = None
        self.size -= 1
        return result

    def resize(self) -> None:
        self.values.extend([None] * self.capacity)
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
