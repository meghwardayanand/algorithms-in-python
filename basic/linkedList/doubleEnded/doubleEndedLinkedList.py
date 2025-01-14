
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtFront(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)

        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def removeFromFront(self):
        if not self.head:
            print("Empty Double Ended LinkedList.")
            return False

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None

        return True

    def removeFromEnd(self):
        if not self.tail:
            print("Empty Double Ended LinkedList.")
            return False

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None

        return True

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
            print("Empty Double Ended LinkedList!")
            return

        while current_node:
            print(f"{current_node.data}", end="")
            if current_node.next:
                print(" <--> ", end="")

            current_node = current_node.next

    def displayReverse(self):
        current_node = self.tail
        if not current_node:
            print("Empty Double Ended LinkedList!")
            return

        while current_node:
            print(f"{current_node.data}", end="")
            if current_node.prev:
                print(" <--> ", end="")

            current_node = current_node.prev

    def __repr__(self):
        current_node = self.head
        if not current_node:
            return "Empty Double Ended LinkedList!"
        
        all_nodes = []
        while current_node:
            all_nodes.append(str(current_node.data))
            current_node = current_node.next
        
        return " <--> ".join(all_nodes)
