

class ListNode:
    def __init__(self, key=-1, val=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

    def connect_next(self, node: "ListNode"):
        node.prev = self
        self.next = node

    def move(self, new_prev_node: "ListNode"):
        prev = self.prev
        next = self.next

        if prev is not None:
            prev.next = next
        if next is not None:
            next.prev = prev

        next = new_prev_node.next
        new_prev_node.next = self
        self.next = next
        self.prev = new_prev_node

    def __str__(self):
        return f"[key: {self.key} val: {self.val}, next: {self.next}]"

class LRUCache:


    def __init__(self, capacity: int):
        self.lookup = {}
        self.capacity = capacity
        self.tail = ListNode(val=None)

        cursor = self.tail
        for _ in range(capacity - 1):
            # print("NODE")
            cursor.connect_next(ListNode(val=None))
            cursor = cursor.next

        self.head = cursor

        # self.print()

    def print(self):
        print(self.tail)

    def create_new_element(self, key: int, value: int):
        node = ListNode(key=key, val=value)
        self.add_node_to_front(node)
        self.lookup[key] = node
        self.pop() 

    def add_node_to_front(self, node: ListNode):

        self.head.connect_next(node)
        self.head = self.head.next

    def move_node_to_front(self, node: ListNode):
        # print("HEAD: ", self.head)
        if node == self.head:
            return
        if node == self.tail and len(self.lookup) > 1:
            self.tail = node.next
        node.move(self.head)
        if len(self.lookup) > 1:
            self.head = self.head.next

    def key_was_accessed(self, key: int):
        self.move_node_to_front(self.lookup[key])

    def pop(self):

        old_key = self.tail.key

        if old_key != -1:
            del self.lookup[old_key]

        self.tail = self.tail.next


    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        
        self.key_was_accessed(key)
        return self.lookup[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.lookup[key].val = value
            self.key_was_accessed(key)
        else:
            self.create_new_element(key, value)

        print("------- end of put -------")
            
        # self.lookup[]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)