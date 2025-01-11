
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        previous_node = self.head
        while previous_node.next:
            previous_node = previous_node.next

        previous_node.next = new_node

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
            print("Empty LinkedList!")
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
            current_node = None
            return True

        previous_node = None
        while current_node and current_node.data != key:
            previous_node = current_node
            current_node = current_node.next

        if not current_node:
            print(f"Node {key} doesn't exist!")
            return False

        previous_node.next = current_node.next
        current_node = None

        return True

    def __repr__(self):
        current_node = self.head
        if not current_node:
            return "Empty LinkedList!"

        all_nodes = []
        while current_node:
            all_nodes.append(f"{current_node.data}")
            current_node = current_node.next

        return " --> ".join(all_nodes)
