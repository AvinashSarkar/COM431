from LINKED_LISTS.node import Node

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def append(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.first.next = new_node
            new_node.prev = self.last
            self.last = new_node

    def get(self, index):
        current = self.first
        current_index = 0

        while current_index is not None:
            if current_index == index:
                return current

            current_index += 1
        return None

    def __str__(self):
        nodes = []
        current = self.first
        while current is not None:
            nodes.append(str(current))
            current = current.next
        return "->".join(nodes)
