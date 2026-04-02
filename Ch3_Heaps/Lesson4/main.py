class MinHeap:
    def push(self, priority, value):
        self.elements.append((priority, value))
        self.bubble_up(len(self.elements) - 1)

    def bubble_up(self, index):
        if index == 0:
            return

        parent_index = (index - 1) // 2
        parent_priority = self.elements[parent_index][0]
        current_priority = self.elements[index][0]

        if parent_priority > current_priority:
            self.elements[parent_index], self.elements[index] = (
                self.elements[index],
                self.elements[parent_index],
            )
            self.bubble_up(parent_index)

    # Don't touch below this line

    def __init__(self):
        self.elements = []

    def peek(self):
        if len(self.elements) == 0:
            return None

        return self.elements[0][1]
