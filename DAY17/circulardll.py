class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next =None
class List:
    def __init__(self):
        self.head = None
        self.tail = None
    def insatbegin(self,val):
        if not self.head :
            self.head = Node(val)
            self.tail = self.head
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            new = Node(val)
            self.head.prev = new
            new.next = self.head
            self.head = new
            self.tail.next = self.head
    def traverse(self):
        temp = self.head
        while temp.next!= self.head:
            print(temp.val)
            temp = temp.next
        print(temp.val)
    def insatend(self,val):
        if not self.head :
            self.head = Node(val)
            self.tail = self.head
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            new = Node(val)
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
            new.next = self.head
            self.head.prev = self.tail
    def delatbeg(self):
        self.head = self.head.next
        self.tail.next = self.head
        self.head.prev = self.tail
    def delatend(self):
        if self.head is not None:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail

lis = List()
lis.insatbegin(1)
lis.insatbegin(2)
lis.insatbegin(3)
lis.insatbegin(4)
lis.insatend(5)
lis.insatend(45)
lis.insatend(63)
lis.delatbeg()
lis.delatend()
lis.traverse()
