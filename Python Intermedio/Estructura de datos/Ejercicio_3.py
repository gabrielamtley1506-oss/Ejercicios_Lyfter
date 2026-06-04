class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        left_h = self._height(node.left)
        right_h = self._height(node.right)
        return 1 + (left_h if left_h > right_h else right_h)

    def print_tree(self):
        if self.root is None:
            print("Empty tree")
            return
        print("In-order:  ", end="")
        self._inorder(self.root)
        print()
        print("Pre-order: ", end="")
        self._preorder(self.root)
        print()
        print("Post-order:", end="")
        self._postorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value, end=" ")
            self._inorder(node.right)

    def _preorder(self, node):
        if node:
            print(node.value, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.value, end=" ")


if __name__ == "__main__":
    bt = BinaryTree()

    for value in [5, 2, 7, 1, 3, 6, 9]:
        bt.insert(value)

    bt.print_tree()

    print(f"\nHeight: {bt.height()}")
    print(f"Search 3: {bt.search(3)}")
    print(f"Search 8: {bt.search(8)}")
