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
    # Time: O(n^A) Space O(1)
    def insertGCD(self,head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next

        while curr:
            gcd = math.gcd(curr.val,prev.val)
            g = ListNode(gcd)
            prev.next = g
            g.next = curr
            prev = curr
            curr = curr.next
        return head

head1 = build_linked_list([18,6,10,3])
head2 = build_linked_list([7])

node = Solution()
node1 = node.insertGCD(head1)
node2 = node.insertGCD(head2)

print(print_list(node1))
print(print_list(node2))