class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class Double_Linked_List():
    def __init__(self):
        self.head = None
        self.pointer = None

    # O(N)
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            print("Append complete")
            return
        
        node = self.head
        while node:
            if not node.next:
                break
            node = node.next
        
        new_node = Node(data)
        new_node.previous = node
        node.next = new_node
        print("Append complete")

    # O(1)
    def left_append(self, data):
        if not self.head:
            self.head = Node(data)
            return

        new_node = Node(data)
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node
        print("Left Append complete" + str(self.head.data))
    
    # O(N)
    def insert_after(self, find_value, data):

        if not self.head:
            print("No nodes in DDL")

        node = self.head
        inserted = False
        while node:
            if node.data == find_value:
                next_node = node.next
                new_node = Node(data)
                new_node.next = next_node
                node.next = new_node
                inserted = True
                print("New Node is inserted")
                break
            node = node.next
        if not inserted:
            print("Value not found. Could not insert.")
    
    def print_nodes(self):
        if not self.head:
            print("No nodes found")

        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    def remove(self, data):
        if not self.head:
            print("No nodes found")

        node = self.head
        deleted = False
        while node:
            if data == node.data:
                previous_node = node.previous
                next_node = node.next
                previous_node.next = next_node
                next_node.previous = previous_node
                deleted = True
                print("Node deleted.")
                break
            node = node.next
        if not deleted:
            print("Node not found")


                
if __name__ == "__main__":
    dll = Double_Linked_List()
    dll.left_append(1)
    dll.left_append(-20)
    dll.left_append(80)
    dll.append(6)
    dll.append(3)
    dll.append(2)
    dll.print_nodes()
    print("~~~~")
    dll.insert_after(3, 5)
    dll.print_nodes()
    dll.remove(1)
    dll.print_nodes()