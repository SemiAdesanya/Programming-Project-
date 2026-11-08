# Task 3: Insert a value in a circular linked list that is sorted in a non descending order
# the node can reference any single node in the list
# it may not be the smallest value...anything works?

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert(head: Node, insertVal: int):  # for an empty line case, then the new node points to itself
    if not head:
        new_node = Node(insertVal)
        new_node.next = new_node
        return new_node

    prev = head
    curr = head.next

    while True:
        if prev.val <= insertVal <= curr.val:    # for a normal case where the value fits
            break                                # between prev and curr

        if prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val):
            break  # for a wrap around case where the insertVal is greater than the max or smaller
                   # than the min
        prev = curr
        curr = curr.next
        if prev is head:  # for when all the elemnets in the list are equal, so we make a full circle
            break         # so the valu ecan be inserted anywhere

    prev.next = Node(insertVal, curr) # to insert a new node between prev and curr and to always 
    return head                       # return the originally given node
                                               
            

# to help convert list to array format for verifivation
def circle(value):  # to build a circular list from a python list, so it returns the first node
    if not value:
        return None
    nodes = [Node(i) for i in value]
    for j in range(len(nodes)):
        nodes[j].next = nodes [(j + 1) % len(nodes)]
    return nodes[0]

        
def circular_list(head): # to walk once around the circle and collect the values
    if not head:
        return[]
    res = [head.val]   # a python list starting with the heads value
    curr = head.next   # a node starting at the second spot
    while curr != head:
        res.append(curr.val)
        curr = curr.next
    return res


# Driver 
if __name__ == "__main__":
    print(circular_list(insert(circle([3, 4, 1]), 2)))   # [3, 4, 1, 2]
    print(circular_list(insert(None, 1)))               # [1]
    print(circular_list(insert(circle([1]), 0)))         # [1, 0]
    print(circular_list(insert(circle([1, 3, 5]), 6)))   # [1, 3, 5, 6]  (new max)
    print(circular_list(insert(circle([3, 5, 1]), 0)))   # new min: 0 goes between 5 and 1 -> [3, 5, 0, 1]
    print(circular_list(insert(circle([2, 2, 2]), 3)))   # all equal = inserted somewhere
