from collections import deque
from sys import maxsize

class Queue():
    def __init__(self, maxsize=10):
        self._queue = deque(maxlen=maxsize)
        
    def enqueue(self, item):
        self._queue.append(item)
    
    def dequeue(self):
        return self._queue.popleft()

if __name__ == "__main__":

    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(10)
    q.enqueue(-1)
    q.enqueue(30)
    q.enqueue(52)
    print(q.dequeue())
    print(q.dequeue())


