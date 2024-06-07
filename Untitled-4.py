class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class Queue:
    def _init_(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        removed_item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_item