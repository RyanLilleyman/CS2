class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return f"""
            {self.queue}
        """

    def is_empty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty."
        return self.queue.pop(0)

    def enqueue(self, t):
        self.queue.append(t)

    def peek(self):
        return self.queue[0]


def main():
    queue = Queue()
    queue.enqueue("hello")
    print(queue)
    queue.dequeue()
    print(queue)


if __name__ == "__main__":
    main()
