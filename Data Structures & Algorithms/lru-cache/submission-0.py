class Node:
    def __init__(self,key=0,value=0):
        self.key =key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add_to_tail(node)
        return node.value
        
    def _remove(self,node:Node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_tail(self,node:Node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev= node

    def put(self, key: int, value: int) -> None:
        # key value
        if key in self.cache:
            self._remove(self.cache[key])
        
        new_node = Node(key,value)
        self.cache[key] = new_node
        self._add_to_tail(new_node)

        if len(self.cache) > self.capacity:
            # remove the least recent head
            # tail recent , head old
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

