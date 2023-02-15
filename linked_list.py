class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def remove_node(self, value):
        node = self.head
        previous = None

        while node is not None:
            if node.data == value:
                if previous is not None:
                    previous.next = node.next
                else:
                    self.head = node.next
                return

            previous = node
            node = node.next

node1 = Node("1")
node2 = Node("2")
node3 = Node("3")

node1.next = node2
node2.next = node3

linked_list = LinkedList()
linked_list.head = node1


new_node = Node("4")
if linked_list.head is None:
    linked_list.head = new_node
else:
    node = linked_list.head
    while node.next is not None:
        node = node.next
    node.next = new_node


linked_list.remove_node("2")

print(linked_list) 