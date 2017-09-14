class Node:

    def __init__(self, initData, initNext):
        self.data = initData
        self.next = initNext


    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next= newNext


class LinkedList:

    def __init__(self):
        self.head=None
        self.size=0

    def isEmpty(self):
        return self.head

    def length(self):
        return self.size

    def append(self, item):
        temp = Node(item, None)
        if (self.head == None):
            self.head = temp
        else:
            current = self.head
            while (current.getNext() != None):
                current = current.getNext()
            current.setNext(temp)
        self.size += 1

    def movetoindex(self, index):
        a = self.head
        while index > 0:
            a = a.next
            index -= 1
        return a
