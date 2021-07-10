    class SList:
        def __init__(self):
            self.head = None
        def add_to_front(self, val):	# added this line, takes a value

        def add_to_front(self, val):
            new_node = SLNode(val)	# create a new instance of our Node class using the given value

    class SLNode:
        def __init__(self, val):
            self.value = val
            self.next = None

        def add_to_front(self, val):
            new_node = SLNode(val)
            current_head = self.head	# save the current head in a variable

        def add_to_front(self, val):
            new_node = SLNode(val)
            current_head = self.head
            new_node.next = current_head	# SET the new node's next TO the list's current head

    	def add_to_front(self, val):
            new_node = SLNode(val)
            current_head = self.head
            new_node.next = current_head
            self.head = new_node	# SET the list's head TO the node we created in the last step
            return self	                # return self to allow for chaining