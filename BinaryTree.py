print("JONATHAN U. URRETE")
print("BSCOE 2-2")
print()

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return  # node already exist 
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data) 
                
    def search(self, val):
            if self.data == val:
             return True

            if val < self.data:
               if self.left:
                 return self.left.search(val)
               else:
                 return True

            if val > self.data:
               if self.right:
                 return self.right.search(val)
               else:
                 return True          
    
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()  
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
    
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
                     
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()     
  
  
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
  
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    
  
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self  
   
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root
print("=======================")
print("BINARY TREE FOR LETTERS")
print("=======================")

if __name__ == '__main__':
    name = ["J", "O", "N", "A", "T", "H", "A", "N", "U", "U", "R", "R", "E", "T", "E"]
    numbers = [13, 15, 24, 6, 19, 28, 35, 45, 20, 9, 1, 45, 41]     
   
name_tree = build_tree(name)
print("Full Name Letters:", name)
print("Minimum value:", name_tree.find_min())
print("Maximum value:", name_tree.find_max())    
print("Is letter J is in the list?:", name_tree.search("J"))
print("Is letter O is in the list?:", name_tree.search("O"))
name_tree.delete("J")
print("After deleting letter J, The ist of letters now shown in order traversal:",
      name_tree.in_order_traversal())
name_tree.delete("N")
print("After deleting letter N, The ist of letters now shown in order traversal",
      name_tree.in_order_traversal())
name_tree.delete("T")
print("After deleting letter T, The ist of letters now shown in order traversal",
      name_tree.in_order_traversal())
print("In order traversal of the list:", name_tree.in_order_traversal())
print("Pre order traversal of the list:", name_tree.pre_order_traversal())
print("Post order traversal of the list:", name_tree.post_order_traversal())

print("=======================")
print("BINARY TREE FOR NUMBERS")
print("=======================")

numbers_tree = build_tree(numbers)
print("numbers:", numbers)
print("Minimum value:", numbers_tree.find_min())
print("Maximum value:", numbers_tree.find_max())
print("Is number 24 is in the list?:", numbers_tree.search(24))
print("Is number 45 is in the list?:", numbers_tree.search(45))
numbers_tree.delete(35)
print("After deleting number 35, The list for numbers now shown in order traversal:",
      numbers_tree.in_order_traversal())
numbers_tree.delete(28)
print("After deleting number 28, The list for numbers now shown in order traversal:",
      numbers_tree.in_order_traversal())
numbers_tree.delete(9)
print("After deleting number 9, The list for numbers now shown in order traversal:",
      numbers_tree.in_order_traversal())
print("Sum of all numbers:", numbers_tree.calculate_sum())
print("In order traversal of the list:", numbers_tree.in_order_traversal())
print("Pre order traversal of the list:",
      numbers_tree.pre_order_traversal())
print("Post order traversal of the list:",
      numbers_tree.post_order_traversal())