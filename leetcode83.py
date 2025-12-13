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
    def deleteDuplicate(self,head: Optional[ListNode]) -> Optional[ListNode]:
     curr = head

     while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
     return head

head1 = build_linked_list([1,1,2])
head2 = build_linked_list([1,1,2,3,3])

node = Solution()
print(print_list(node.deleteDuplicate(head1)))
print(print_list(node.deleteDuplicate(head2)))