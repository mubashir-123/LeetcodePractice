from typing import Optional

class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

# Helper to convert list → linked list
def build_list_with_cycle(arr, pos):
    if not arr:
        return None
    
    # Create the head
    head = ListNode(arr[0])
    curr = head
    nodes = [head] # Keep track of nodes to link back later
    
    # Build the linear list
    for num in arr[1:]:
        new_node = ListNode(num)
        curr.next = new_node
        curr = new_node
        nodes.append(curr)
    
    # Create the cycle if pos is valid
    if pos != -1 and pos < len(nodes):
        # Connect the last node (curr) to the node at index 'pos'
        curr.next = nodes[pos]
        
    return head

# Helper to print linked list
def print_list_safe(head, limit=10):
    curr = head
    result = []
    count = 0
    while curr and count < limit:
        result.append(curr.val)
        curr = curr.next
        count += 1
    
    output = " -> ".join(map(str, result))
    if curr: # If there is still more attached (likely a cycle)
        output += " -> ..."
    return output

class Solution:
    def hasCycle(self,head: Optional[ListNode]) -> Optional[ListNode]:
        # Floyd's Tortoise and Hare" algorithm
        # Time O(n)
        # Space O(1)
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow is fast:
                return True
        return False

node = Solution()

list1 = build_list_with_cycle([3,2,0,-4],1)
list2 = build_list_with_cycle([1,2],0)
list3 = build_list_with_cycle([],-1)

print(print_list_safe(list1))
print(print_list_safe(list2))
print(print_list_safe(list3))

print(node.hasCycle(list1))
print(node.hasCycle(list2))
print(node.hasCycle(list3))