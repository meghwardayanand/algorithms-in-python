
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtFront(self, data):
        new_node = Node(data)
        if self.head:
            self.head.previous = new_node

        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        new_node.previous = current_node

    def isFound(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next

        return False

    def find(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return current_node
            current_node = current_node.next

        return None

    def display(self):
        current_node = self.head
        if not current_node:
            print("Empty Doubly LinkedList!")
            return

        while current_node:
            print(f"{current_node.data}", end="")
            if current_node.next:
                print(" --> ", end="")
            current_node = current_node.next

    def delete(self, key):
        current_node = self.head

        if current_node and current_node.data == key:
            self.head = current_node.next
            if self.head:
                self.head.previous = None

            current_node = None
            return True

        while current_node and current_node.data != key:
            current_node = current_node.next

        if not current_node:
            print(f"Node {key} doesn't exist!")
            return False

        if current_node.next:
            current_node.next.previous = current_node.previous

        if current_node.previous:
            current_node.previous.next = current_node.next

        current_node = None
        return True

    def displayReverse(self):
        current_node = self.head
        if not current_node:
            print("Empty Doubly LinkedList!")
            return

        while current_node.next:
            current_node = current_node.next

        while current_node:
            print(f"{current_node.data}", end="")
            if current_node.previous:
                print(" --> ", end="")

            current_node = current_node.previous

    def __repr__(self):
        current_node = self.head
        if not current_node:
            return "Empty Doubly LinkedList!"

        all_nodes = []
        while current_node:
            all_nodes.append(f"{current_node.data}")
            current_node = current_node.next

        return " --> ".join(all_nodes)
