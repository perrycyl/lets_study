class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList():
    def __init__(self):
        self.head = None
    
    def print_llist(self):
        if self.head == None:
            print("None")
            return
        
        node = self.head
        while node:
            print(node.data)
            if not node.next:
                break
            node = node.next
        
    # add data to end of linked list
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            print(f"Appended-new: {data}")
            return
        
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)
        print(f"Appended: {data}")

    # add data to the start of the linked list
    def left_append(self, data):
        if not self.head:
            self.head = Node(data)
        
        new_head_next = self.head
        self.head = Node(data)
        self.head.next = new_head_next

if __name__ == "__main__":
    llist = LinkedList()
    llist.append(12)
    llist.append(5)
    llist.append(7)
    llist.append(7)
    llist.append(33)
    llist.append(50)
    llist.print_llist()
    print("~~~~\n")
    llist.left_append(-1)
    llist.left_append(1000)
    llist.print_llist()



