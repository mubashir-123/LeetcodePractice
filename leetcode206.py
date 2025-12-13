from typing import Optional

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
    def reverseList(self,head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

head1 = build_linked_list([1,2,3,4,5])
head2 = build_linked_list([1,2])
head3 = build_linked_list([])

node = Solution()
print(print_list(node.reverseList(head1)))
print(print_list(node.reverseList(head2))) 
print(print_list(node.reverseList(head3))) 