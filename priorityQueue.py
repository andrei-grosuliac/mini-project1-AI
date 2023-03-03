class PriorityQueue:
    def __init__(self):
        self.items = []

    def put(self, priority, item):
        """Insert an item with a given priority value."""
        i = 0
        while i < len(self.items) and self.items[i][0] <= priority:
            i += 1
        self.items.insert(i, (priority, item))


    def get(self):
        """Remove and return the item with the lowest priority value."""
        return self.items.pop(0)[1]

    def empty(self):
        """Return True if the queue is empty, else False."""
        return len(self.items) == 0