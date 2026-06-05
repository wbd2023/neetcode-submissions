class LinkedList:
    data: Any
    next: LinkedList

    def __init__(self):
        self.data = None
        self.next = None

    def get(self, index: int) -> int:
        if index == 0:
            return self.data

        if self.next == None:
            return -1

        return self.next.get(index - 1)

    def insertHead(self, val: int) -> None:
        new = LinkedList()

        # Make new a clone of self
        if self != None:
            new.next = self.next
            new.data = self.data

        # Make self the new head, pointing to the clone
        self.data = val
        self.next = new

    def insertTail(self, val: int) -> None:
        current = self
        while current.next != None:
            current = current.next

        new = LinkedList()
        new.data = val

        current.next = new

    def remove(self, index: int) -> bool:
        if index == 0:
            if self.next:

                self.next = self.next.next
                self.data = self.next.data
                return True
            else:
                self.data = None
                return True
        i = 0
        current = self
        current = self

        i += 1
        while current is not None and i < index - 1:
            current = current.next
        
        if current.next:
            current.next = current.next.next


        if self.data is None: return []

    def getValues(self) -> List[int]:
        result = [self.data]
        if self.next != None:
            result.extend(self.next.getValues())

        return result
