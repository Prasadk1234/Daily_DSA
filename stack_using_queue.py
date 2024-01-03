from queue import Queue


class MyStack:

    def __init__(self):
        self.insert_queue = Queue()
        self.shuffle_queue = Queue()
        self.stack_length = 0

    def push(self, x: int) -> None:
        self.insert_queue.put(x)

        while not self.shuffle_queue.empty():
            self.insert_queue.put(
                self.shuffle_queue.get()
            )

        tem = self.insert_queue
        self.insert_queue = self.shuffle_queue
        self.shuffle_queue = tem
        self.stack_length = self.stack_length + 1

        return None

    def pop(self) -> int:
        if (self.shuffle_queue.empty()):
            return 0
        else:
            item = self.shuffle_queue.get()
            self.stack_length -= 1
            return item

    def top(self) -> int:
        if (self.shuffle_queue.empty()):
            return None
        return self.shuffle_queue.queue[0]

    def empty(self) -> bool:
        return self.stack_length == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()