from STACKS.stack import Stack

def main():
    stack1 = Stack()
    stack1.push(1)
    stack1.push(4)
    stack1.push(9)
    print(stack1)

    popped1 = stack1.pop()
    print(popped1)
    popped2 = stack1.pop()
    print(popped2)

    print(stack1)

    stack2 = Stack()
    stack2.push("Linux")
    stack2.push("Windows")
    stack2.push("Mac OS X")

    print(stack2)

    top_item = stack2.peek()
    print(top_item)

    popped3 = stack2.pop()
    print(popped3)

    print(stack2)

if __name__ == '__main__':
    main()