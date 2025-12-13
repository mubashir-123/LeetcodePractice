from typing import Optional

class ListNode:
    """
    Modified Node structure to include a 'random' pointer.
    """
    def __init__(self, val=0, next_node: 'ListNode'=None, random_node: 'ListNode'=None):
        self.val = val
        self.next = next_node
        self.random = random_node

    def __repr__(self):
        """A simple representation for printing/verification."""
        random_val = self.random.val if self.random else 'null'
        return f"[{self.val}, {random_val}]"

# Helper to create list of nodes with random pointers
def build_random_linked_list(arr_with_randoms):
    """
    Converts input array of [[val, random_index], ...] into a linked list
    with connected 'next' and 'random' pointers.
    """
    if not arr_with_randoms:
        return None

    # --- Pass 1: Create all nodes and map index to node object ---
    # node_map: {index (0, 1, 2, ...): ListNode object}
    node_map = {}
    head = None
    current = None
    
    for i in range(len(arr_with_randoms)):
        val, _ = arr_with_randoms[i]
        
        # 1. Create the new node
        new_node = ListNode(val)
        
        # 2. Add it to the map using its list index
        node_map[i] = new_node
        
        # 3. Build the 'next' structure
        if head is None:
            head = new_node
            current = head
        else:
            current.next = new_node
            current = new_node
            
    # --- Pass 2: Set the random pointers using the map ---

    for i in range(len(arr_with_randoms)):
        # Get the node we need to update from the map
        current_node = node_map[i]
        
        # Get the random index target from the input data
        _, rand_index = arr_with_randoms[i]
        
        if rand_index is not None:
            # Look up the target node object in the map
            random_target_node = node_map.get(rand_index)
            # Set the random pointer
            current_node.random = random_target_node
        
    return head

# Helper to print linked list structure (with random pointers)
def print_list(head):
    """Prints the list structure showing value and random target."""
    curr = head
    result = []
    while curr:
        result.append(curr)
        curr = curr.next
    return result

class Solution:
    def copyRandomList(self,head: 'Optional[ListNode]' ) -> 'Optional[ListNode]':
        if not head: return None

        curr = head
        old_to_new = {}

        while curr:
            node = ListNode(val = curr.val)
            old_to_new[curr] = node
            curr = curr.next

        curr = head

        while curr:
            new_node = old_to_new[curr]
            new_node.next = old_to_new[curr.next] if curr.next else None 
            new_node.random = old_to_new[curr.random] if curr.random else None
            curr = curr.next

        return old_to_new[head] 


# --- Example Usage (Using the structure from your original image) ---
# Input: [[7,null], [13,0], [11,4], [10,2], [1,0]]
input_data1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
input_data2 = [[1,1],[2,1]]
input_data3 = [[3,None],[3,0],[3,None]]

print(f"Input Data: {input_data1}")
list_head1 = build_random_linked_list(input_data1)
output1 = print_list(list_head1)
print(f"Created List (Value, Random Target): {output1}")

print(f"Input Data: {input_data2}")
list_head2 = build_random_linked_list(input_data2)
output2 = print_list(list_head2)
print(f"Created List (Value, Random Target): {output2}")

print(f"Input Data: {input_data3}")
list_head3 = build_random_linked_list(input_data3)
output3 = print_list(list_head3)
print(f"Created List (Value, Random Target): {output3}")

node = Solution()
print('------------------------------------------------------------------------------------------------')
print(print_list(node.copyRandomList(list_head1)))
print(print_list(node.copyRandomList(list_head2)))
print(print_list(node.copyRandomList(list_head3)))

