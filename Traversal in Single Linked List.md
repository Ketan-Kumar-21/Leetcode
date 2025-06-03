class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def traverse_and_join(self):
        temp = self.head
        result = []
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(result))

