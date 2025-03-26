class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None

class Solution:
    def constructLL(self, arr):
        if not arr:
            return None
        self.head = Node(arr[0])
        current = self.head
        for value in arr[1:]:
            current.next = Node(value)
            current = current.next
        return self.head  

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")  
            current = current.next
        print("None")  
