from collections import deque
class queue:
    def __init__(self):
        self.item=deque()
    def enqueue(self,val):
        self.item.append(val)
    def dequeue(self):
        if self.item==None:
            return
        else:
            self.item.popleft()
