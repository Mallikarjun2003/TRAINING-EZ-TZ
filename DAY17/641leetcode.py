class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [0] * k
        self.count = 0
        self.size = k

    def insertFront(self, value: int) -> bool:
        if self.count >= self.size:
            return False
        self.count += 1
        self.deque.insert(0, value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.count >= self.size:
            return False
        self.count += 1
        self.deque.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.count == 0:
            return False
        self.count -= 1
        self.deque.pop(0) 
        return True

    def deleteLast(self) -> bool:
        if self.count == 0:
            return False
        self.count -= 1
        self.deque.pop() 
        return True

    def getFront(self) -> int:
        if self.count == 0:
            return -1
        return self.deque[0]

    def getRear(self) -> int:
        if self.count == 0:
            return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size
