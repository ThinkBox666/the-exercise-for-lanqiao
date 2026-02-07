class Node:
     def __init__(self,val):
         self.val=val
         self.lt=None
         self.rt=None
def preorder(node):
    if node is None:
        return
    else:
        print(node.val,end='=>')
        preorder(node.lt)
        preorder(node.rt)
def inorder(node):
    if node is None:
        return
    else:
        inorder(node.lt)
        print(node.val)
        inorder(node.rt)
def posterorder(node):
    if node is None:
        return
    else:
        posterorder(node.lt)
        posterorder(node.rt)
        print(node.val)
