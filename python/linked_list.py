import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_median(linked_list):
    mapper = {}
    count = 0
    temp = linked_list
    while temp != None:
        count += 1
        mapper[count] = temp.data
        temp = temp.next
    
    return mapper[math.ceil(count/2)]

def removeNthFromEnd(head, n):
    count = 0
    temp = head 
    while temp != None:
        count += 1
        temp = temp.next

    index = count - (n-1)

    if index == 1:
        node_to_remove = head
        head = head.next
        del node_to_remove
        return head

    count = 1
    temp = head
    while count != index-1:
        count += 1
        temp = temp.next
    
    node_to_remove = temp.next
    temp.next = node_to_remove.next
    node_to_remove.next = None

    return head

        

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

print("MEDIAN IS ", find_median(head))
removeNthFromEnd(head, 2)

