class Node():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class Linkednode():
    def __init__(self,head=None):
        self.head=head
    def append(self,val):
        node=Node(val)
        if self.head==None:
            self.head=node
            return
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=node
            return
    def preappend(self,val):
        node=Node(val)
        if self.head==None:
            self.head=node
            return
        else:
            node.next=self.head
            self.head=node
    def insert(self,where,val):
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
            return
    def delete(self,val):
        if self.head==val:
            self.head=self.head.next
        elif self.head==None:
            return 0
        else:
            current=self.head
            while current.next:
                if current.next.val==val:
                    current.next=current.next.next
                    return
                else:
                    current=current.next
            return -1
    def display(self):
        elements=[]
        if self.head==None:
            return None
        current=self.head
        while current.next:
            elements.append(str(current.val))
            current=current.next
        print('=>'.join(elements))
if __name__=='__main__':
    nodelist=Linkednode()
    for i in range(10):
        nodelist.append(i)
    nodelist.preappend(200)
    nodelist.insert(3,1000)
    nodelist.delete(8)
    nodelist.display()




