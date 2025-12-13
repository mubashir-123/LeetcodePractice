from typing import Optional
import math 

class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

# Helper to convert list → linked list
def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for num in arr[1:]:
        curr.next = ListNode(num)
        curr = curr.next
    return head

# Helper to print linked list
def print_list(head):
    curr = head
    result = []
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

class Solution:
    # Time: O(n) Space O(1)
    def removeNthFromNode(self,head: Optional[ListNode],n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        behind = ahead = dummy

        for _ in range(n + 1):
            ahead = ahead.next
        
        while ahead:
            behind = behind.next
            ahead = ahead.next
        
        behind.next = behind.next.next
        return dummy.next

list1 = build_linked_list([1,2,3,4,5])
list2 = build_linked_list([1])
list3 = build_linked_list([1,2])

node = Solution()
node1 = node.removeNthFromNode(list1,2)
node2 = node.removeNthFromNode(list2,1)
node3 = node.removeNthFromNode(list3,1)

print(print_list(node1))
print(print_list(node2))
print(print_list(node3))

