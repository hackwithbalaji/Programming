class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



head = Node(1)

temp = head 
for i in range(0,9):
    new_node = Node(i+2)
    temp.next = new_node
    temp = temp.next

printNode = head
while printNode != None:
    print(printNode.data)
    printNode = printNode.next

