class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        self._size -= 1
        return value

    def size(self):
        return self._size

    def __repr__(self):
        elements = ""
        current = self.top
        while current is not None:
            elements += str(current.value)
            if current.next is not None:
                elements += " -> "
            current = current.next
        return f"Stack(top -> {elements})"


if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)         
    print(stack.pop())   
    print(stack.size())  
    print(stack)         