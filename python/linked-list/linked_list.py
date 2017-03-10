# Skeleton file for the Python "linked-list" exercise.
# Implement the LinkedList class


class Node(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
    def __str__(self):
        return '{}'.format(self.value)


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        self.current = self.head
        return self
    def next(self):
        if self.current is None:
            raise StopIteration
        else:
            curr = self.current
            self.current = self.current.next
        return curr.value
    def __len__(self):
        l = 0
        for node in self:
            if node is None: break
            else: l += 1
        return l
    def __str__(self):
        return '<->'.join(str(node) for node in self)
    def push(self, value):
        if self.tail is None:
            self.head = self.tail = Node(value)
        else:
            new_tail = Node(value)
            self.tail.next = new_tail
            new_tail.prev = self.tail
            self.tail = new_tail
    def pop(self):
        old_tail = self.tail
        self.tail = self.tail.prev
        if self.tail is not None: self.tail.next = None
        else: self.head = self.tail
        return old_tail.value
    def shift(self):
        old_head = self.head
        self.head = self.head.next
        if self.head is not None: self.head.prev = None
        else: self.tail = self.head
        return old_head.value
    def unshift(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            new_head = Node(value)
            self.head.prev = new_head
            new_head.next = self.head
            self.head = new_head
