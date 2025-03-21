class Stack:
    def __init__(self):
        self.stack = []

    def push(self,value):
        self.stack.append(value)
    
    def pop(self):
        if not self.stack:
            print("Stack is Empty")
        del self.stack[-1]
    
    def top(self):
        return self.stack[-1]

    def is_empty(self):
        if not self.stack:
            return True
        return False

    def size(self):
        size = len(self.stack)
        return size
    
    def __str__(self):
        return f"Stack = {self.stack}"


if __name__ == "__main__":

    tower_of_hanoi= Stack()

    tower_of_hanoi.push(40) 
    tower_of_hanoi.push(30) 
    tower_of_hanoi.push(20)
    tower_of_hanoi.push(10)
    tower_of_hanoi.pop() 

    print(f"Top element: {tower_of_hanoi.top()}")
    print(f"is Empty: {tower_of_hanoi.is_empty()}")
    print(f"size: {tower_of_hanoi.size()}")
    print(tower_of_hanoi)