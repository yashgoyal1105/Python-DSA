class Queue:
    def __init__(self):
        self.queue = []
    
    def __str__(self):
        return f"Queue = {self.queue}"
    
    def enqueue(self,value):
        self.queue.append(value)
        return self.queue
    
    def dequeue(self):
        if not self.queue:
            return "Queue is Empty"
        del self.queue[0]

    def peek(self):
        return self.queue[0]
    
    def isEmpty(self):
        if not self.queue:
            return True
        return False
    
    def size(self):
        size = len(self.queue)
        return size

if __name__ == "__main__":
    Movie_tickets = Queue()
    Movie_tickets.enqueue(2)
    Movie_tickets.enqueue(4)
    Movie_tickets.enqueue(5)
    Movie_tickets.enqueue(6)    
    Movie_tickets.enqueue(9)
    Movie_tickets.dequeue()

    print(f"Peek is : {Movie_tickets.peek()}")
    print(f"If Queue is Empty: {Movie_tickets.isEmpty()}")
    print(f"size: {Movie_tickets.size()}")

    print(Movie_tickets)
