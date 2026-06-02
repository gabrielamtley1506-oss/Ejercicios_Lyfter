class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_left(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def push_right(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop_left(self):
        if self.head is None:
            raise IndexError("pop_left from an empty deque")
        value = self.head.value
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return value

    def pop_right(self):
        if self.tail is None:
            raise IndexError("pop_right from an empty deque")
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return value

    def print_deque(self):
        if self.head is None:
            print("Empty deque")
            return
        current = self.head
        elements = ""
        while current is not None:
            elements += str(current.value)
            if current.next is not None:
                elements += " <-> "
            current = current.next
        print(f"[{elements}]")


if __name__ == "__main__":
    dq = Deque()

    dq.push_right(1)
    dq.push_right(2)
    dq.push_right(3)
    dq.push_left(0)
    dq.push_left(-1)
    dq.print_deque()   

    print("pop_left:", dq.pop_left())   
    print("pop_right:", dq.pop_right()) 
    dq.print_deque() 
