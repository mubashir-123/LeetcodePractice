# --------------- Singly Linked List ----------------
class Node: # Strucuture of the Node to create a node of the link list
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class SinglyList: # class to create, add singly link list
    def __init__(self):
        self.head = None # initializing the head

    # O(n) times
    def append(self,val):

        new_node = Node(val) # Creating new_node

        if not self.head: # Appending first node
           self.head = new_node
           return
        
        curr = self.head 

        while curr.next: # This loop finds the last node and then append the new_node
            curr = curr.next # Pointing to the next addres of the node
        curr.next = new_node  # Appending the new_node to the pointing address


    def search(self,val): 

        curr = self.head # start from the head to traverse

        while curr:  # loop until current points to None

          if val == curr.val:  # Logic to find the given value and search value in list to match 
            return print(curr.val) # Return if value finds
          curr = curr.next # pointing to the next node address to loop the entire list

        return print("No node found")  # prints when no match found   
    

    def display(self): # This function taverse the nodes and return the list      

        current = self.head    # Points to the first node of the list 
        result = []   # initailize he list which return the final list of elements

        while current:  # loops the values until current points to the None and stops
            result.append(current.val)  # add the current node value in list
            current = current.next      # points to the next element
        return result
            

    # O(1) times
    def prepend(self,val): # to add new node in begining
        first_node = Node(val) # craete new node
        first_node.next = self.head # link new node to the curent node
        self.head = first_node  # updating the list start point  




sll = SinglyList()
sll.append(1)        
sll.append(2)        
sll.append(5)        
sll.append(7)
sll.prepend(3)

content_display = SinglyList.display(sll)
print(content_display)       
search_node = sll.search(5)



