import copy as c


class Queue:
    def __init__(self, *args):
        self.queue = list(args)

    def append(self, *values):
        self.queue.extend(values)

    def extend(self, other):
        self.queue.extend(other.queue)

    def copy(self):
        return c.deepcopy(self)

    def pop(self):
        return self.queue.pop(0) if self.queue else None

    def __iter__(self):
        return self

    def __next__(self):
        return Queue(*self.queue[1:])

    def next(self):
        return next(self)

    def __add__(self, other):
        return Queue(*(self.queue + other.queue))

    def __iadd__(self, other):
        self.queue += other.queue
        return self

    def __eq__(self, other):
        return self.queue == other.queue

    def __rshift__(self, other):
        return Queue(*self.queue[other:])

    def __str__(self):
        return "[" + " -> ".join(map(str, self.queue)) + "]"
