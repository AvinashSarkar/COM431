class Stack:
    def __init__(self):
        self.internal_list = []

    def push(self, item):
        self.internal_list.append(item)

    def pop(self):
        if self.internal_list:
            return self.internal_list.pop()
        else:
            return None

    def peek(self):
        if self.internal_list:
            return self.internal_list[-1]
        else:
            return None

    def __str__(self):
        return str(self.internal_list)

