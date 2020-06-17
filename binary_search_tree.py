# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/?ref=lbp
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
  
# A utility function to insert a new node with given key in BST 
def insert(node, key): 
  
    # If the tree is empty, return a new node 
    if node is None: 
        return Node(key) 
  
    # Otherwise recur down the tree 
    if key < node.key: 
        node.left = insert(node.left, key) 
    else: 
        node.right = insert(node.right, key) 
  
    # return the (unchanged) node pointer 
    return node 
  
# A utility function to find the node containing the minimum key in BST.
def minValueNode( node): 
    current = node 
  
    # loop down to find the leftmost leaf 
    while(current.left is not None): 
        current = current.left  
  
    return current  
  
# A utility function to delete a node with given key in BST
def deleteNode(root, key): 
  
    # Base Case 
    if root is None: 
        return root  
  
    # If the key to be deleted is smaller than the root's 
    # key then it lies in  left subtree 
    if key < root.key: 
        root.left = deleteNode(root.left, key) 
  
    # If the kye to be delete is greater than the root's key 
    # then it lies in right subtree 
    elif(key > root.key): 
        root.right = deleteNode(root.right, key) 
  
    # If key is same as root's key, then this is the node 
    # to be deleted 
    else: 
          
        # Node with only one child or no child 
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
  
        # Node with two children: Get the inorder successor 
        # (smallest in the right subtree) 
        temp = minValueNode(root.right) 
  
        # Copy the inorder successor's content to this node 
        root.key = temp.key 
  
        # Delete the inorder successor 
        root.right = deleteNode(root.right , temp.key) 
  
  
    return root
