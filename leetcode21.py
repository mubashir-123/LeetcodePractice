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
    def mergeTwoList(self,list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # d = ListNode()
        # curr = d

        # while list1 and list2:
        #     if list1.val < list2.val:
        #         curr.next = list1
        #         curr = list1
        #         list1 = list1.next
        #     else:
        #         curr.next = list2
        #         curr = list2
        #         list2 = list2.next
        
        # curr.next = list1 if list1 else list2
        # return d.next

        d = ListNode()
        curr = d
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        curr.next = list1 if list1 else list2
        return d.next
    
list1 = build_linked_list([1,2,4])
list2 = build_linked_list([1,3,4])

list3 = build_linked_list([])
list4 = build_linked_list([])

list5 = build_linked_list([])
list6 = build_linked_list([0])

node = Solution()
print(print_list(node.mergeTwoList(list1, list2)))
print(print_list(node.mergeTwoList(list3,list4))) 
print(print_list(node.mergeTwoList(list5,list6))) 