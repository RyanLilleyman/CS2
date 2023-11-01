class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return f"""
             {self.stack}
        """

    def push(self, t):
        self.stack.append(t)

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]


def main():
    stack = Stack()
    toPush = "hello"
    stack.push(toPush)
    print(stack)
    print(stack.peek())
    print(stack.pop())
    print(stack)


if __name__ == "__main__":
    main()
