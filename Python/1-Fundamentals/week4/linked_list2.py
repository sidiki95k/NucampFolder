class Node:
  def __init__(self, value):
    self .value = value
    self .next = None

def iter_linked_list(node):
    while node is not None:
        print(node.value)
        node = node.next

head = Node("1st Node")
head .next= Node("2nt Node")
head.next.next = Node("3rt Node")
head.next.next.next = Node("4th Node")

iter_linked_list(head)
head.next.next.next = Node("4th Node")
