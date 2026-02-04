class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class linkedNode:
    def __init__(self,head):
        self.head=None
    def prend(self,val):
        node=Node(val)
        if self.head==None:
            self.head=node
            return
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=node
    def preprend(self,val):
        node=Node(val)
        node.next=self.head
        self.head=node
    def inser(self,where,val):
        node=Node(val)
        if self.head==None:
            self.head=node
            return
        else:
            current=self.head
            for i in range(where-1):
                current=current.next
            node.next=current.next
            current.next=node












