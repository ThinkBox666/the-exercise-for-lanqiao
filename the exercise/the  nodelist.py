class Nodelist:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class linkedlist:
    def __init__(self,head=None):
        self.head=head
    def append(self,val):
        new_node=Nodelist(val)
        if self.head==None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
    def preappend(self,val):
        new_node=Nodelist(val)
        new_node.next=self.head
        self.head=new_node

