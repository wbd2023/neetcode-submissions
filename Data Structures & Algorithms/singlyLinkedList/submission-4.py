class Node:
    value: int
    next: Node | None

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f"Node(value={self.value}, next={self.next})"


class LinkedList:
    head: Node | None

    def __init__(self):
        self.head = None

    def isEmpty(self):
        print(self)
        return not self.head

    def get(self, index: int) -> int:
        if self.isEmpty():
            return -1

        count = 0
        current = self.head

        while current and count < index:
            count += 1
            current = current.next

        if current and count == index:
            return current.value

        return -1

    def insertHead(self, val: int) -> None:
        new = Node(val)

        if not self.isEmpty():
            new.next = self.head

        self.head = new

    def insertTail(self, val: int) -> None:
        new = Node(val)

        if self.isEmpty():
            self.head = new
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new

    def remove(self, index: int) -> bool:
        if self.isEmpty():
            return False

        count = 0
        previous = None
        current = self.head

        while current and count < index:
            count += 1
            previous = current
            current = current.next

        if count == index:
            if current == self.head:
                self.head = None
                return True

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

    def __repr__(self) -> str:
        return f"LinkedList(head={self.head})"
