
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtFront(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next

            current_node.next = new_node
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next

            current_node.next = new_node
            new_node.next = self.head

    def removeFromFront(self):
        if not self.head:
            print("Circular Linked List is empty!")
            return False

        if self.head.next == self.head:
            self.head = None
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next

            current_node.next = self.head.next
            self.head = self.head.next

        return True

    def removeFromEnd(self):
        if not self.head:
            print("Circular Linked List is empty!")
            return False

        if self.head.next == self.head:
            self.head = None
        else:
            current_node = self.head
            previous_node = None
            while current_node.next != self.head:
                previous_node = current_node
                current_node = current_node.next

            previous_node.next = self.head

        return True

    def isFound(self, key):
        if not self.head:
            return False

        current_node = self.head
        while True:
            if current_node.data == key:
                return True

            current_node = current_node.next
            if current_node == self.head:
                break

        return False

    def find(self, key):
        if not self.head:
            return None

        current_node = self.head
        while True:
            if current_node.data == key:
                return current_node

            current_node = current_node.next
            if current_node == self.head:
                break

        return None

    def display(self):
        if not self.head:
            print("Empty Circular LinkedList!")
            return

        current_node = self.head
        while True:
            print(f"{current_node.data}", end="")
            current_node = current_node.next
            if current_node == self.head:
                print(f" --> (head)", end="")
                break

            print(" --> ", end="")

    def __repr__(self):
        if not self.head:
            return "Empty Circular LinkedList!"

        current_node = self.head
        all_nodes = []
        while True:
            all_nodes.append(str(current_node.data))
            current_node = current_node.next
            if current_node == self.head:
                all_nodes.append("(head)")
                break

        return " --> ".join(all_nodes)
