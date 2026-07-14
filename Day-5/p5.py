'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def linked_list():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    return head
head = linked_list()
temp = head 
while temp is not None:
    print(temp.data)
    temp = temp.next'''
class Node:
    def __init__(self, data ):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root == None:
        return Node(data)
    elif data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root
root = None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)


v = [10, 5, 15, 3, 7, 12, 18]
for i in v:
    root = insert(root, i)

insert(root, 25)
insert(root, 8)
insert(root, 100)
print(root.data)
inorder(root)
