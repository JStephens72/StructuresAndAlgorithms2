class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def push(self, priority, item):
        self.elements.append((priority, item))

    def pop(self):
        if self.empty():
            return None

        min_index_so_far = 0
        for i in range(len(self.elements)):
            if self.elements[i][0] < self.elements[min_index_so_far][0]:
                min_index_so_far = i

        item = self.elements[min_index_so_far][1]
        del self.elements[min_index_so_far]
        return item
