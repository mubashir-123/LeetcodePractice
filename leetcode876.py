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
    # Time: O(n) Space O(1)
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

head1 = build_linked_list([1,2,3,4,5])
head2 = build_linked_list([1,2,3,4,5,6])

node = Solution()

list1 = node.middleNode(head1)
list2 = node.middleNode(head2)

print(print_list(list1))
print(print_list(list2))