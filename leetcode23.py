import heapq
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for num in arr[1:]:
        curr.next = ListNode(num)
        curr = curr.next
    return head

def buildLinkedLists(lists):
    result = []
    for arr in lists:
        result.append(build_linked_list(arr))
    return result


# Helper to print linked list
def printLinkedList(head):
    while head:
        print(head.val, end=" → ")
        head = head.next
    print("None")


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        # heap = []
        # # k logk (the stack will store k times)
        # for i,node in enumerate(lists):
        #     if node:
        #         heapq.heappush(heap,(node.val,i,node))
        
        # D = ListNode()
        # curr = D

        # # n logk (all elements will be merge with heap of k times)
        # while heap:
        #     val,i,node = heapq.heappop(heap)
        #     curr.next = node
        #     curr = node
        #     node = node.next

        #     if node:
        #         heapq.heappush(heap,(node.val,i,node))

        # return D.next
        # # Time  O(n logk final) space O(k)

        heap = []

        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))
        
        d = ListNode()
        curr = d

        while heap:
            val,i,node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(heap,(node.val,i,node))
        return d.next

sol = Solution()

lists1 = [[1,4,5], [1,3,4], [2,6]]
linked_lists1 = buildLinkedLists(lists1)

for l in linked_lists1:
    printLinkedList(l)

print()

result1 = sol.mergeKLists(linked_lists1)
printLinkedList(result1)

lists2 = []
linked_lists2 = buildLinkedLists(lists2)

for l in linked_lists2:
    printLinkedList(l)

print()

result2 = sol.mergeKLists(linked_lists2)
printLinkedList(result2)

lists3 = [[]]
linked_lists3 = buildLinkedLists(lists3)

for l in linked_lists3:
    printLinkedList(l)

print()

result3 = sol.mergeKLists(linked_lists3)
printLinkedList(result3)