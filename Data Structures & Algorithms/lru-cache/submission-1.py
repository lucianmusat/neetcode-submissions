class Node:
    def __init__(self, key = 0, value=0, nxt=None, prev=None):
        self.key = key
        self.value = value
        self.nxt  = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # Use a hashmap for O(1) operations
        # And a linked list to store the data and keep track of the LRU and MRU
        self.cache = {}  # store key and ptr to node
        self.capacity = capacity
        self.mru_node, self.lru_node = Node(), Node()
        self.lru_node.nxt = self.mru_node
        self.mru_node.prev = self.lru_node

    def get(self, key: int) -> int:
        # Get the value if it exists, and update the node to be MRU
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # Removing and adding will make sure to mark it as MRU
        self.remove(node)
        self.add(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the existing node's value and mark as MRU
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.add(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.add(node)
        # Evict the LRU if we go over capacity
        if len(self.cache) > self.capacity:
            print("Over capacity, popping the LRU")
            lru = self.lru_node.nxt
            self.remove(lru)
            del self.cache[lru.key]
    
    def add(self, node: Node) -> None:
        node.prev = self.mru_node.prev
        node.nxt = self.mru_node
        self.mru_node.prev.nxt = node
        self.mru_node.prev = node
    
    def remove(self, node: Node) -> None:
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev




