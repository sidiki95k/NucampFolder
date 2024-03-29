class Node:
  def __init__(self, value):
    self .value = value
    self .next = None

head = Node("1st Node")
head .next= Node("2nt Node")
head.next.next = Node("3rt Node")
head.next.next.next = Node("4rt Node")

print(head.value)
print(head.next.value)
print(head.next.next.value)
print(head.next.next.next.value)
