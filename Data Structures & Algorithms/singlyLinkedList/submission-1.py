class Node:
    value: int
    next: Node | None

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    head: Node | None

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return not self.head

    def get(self, index: int) -> int:
        if self.isEmpty():
            return -1

        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count if current else -1

    def insertHead(self, val: int) -> None:
        new = Node(val)

        if not self.isEmpty():
            new.next = self.head

        self.head = new

    def insertTail(self, val: int) -> None:
        new = Node(val)

        previous = None
        current = self.head

        while current:
            previous = current
            current = current.next

        previous.next = new

    def remove(self, index: int) -> bool:
        count = 0
        previous = None
        current = self.head

        while current and count < index:
            count += 1
            previous = current
            current = current.next

        if count == index:
            previous.next = current.next
            return True

        return False

    def getValues(self) -> List[int]:
        result = list()
        current = self.head

        while current:
            result.append(current.value)
            current = current.next

        return result
