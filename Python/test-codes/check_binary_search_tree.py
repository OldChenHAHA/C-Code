
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check_binary_search_tree_(root):
    return check_node(root,float('-inf'),float('inf'))

def check_node(root,min,max):
    if root is None:
        return True
    if root.data <= min or root.data >= max :
        return False
    return check_node(root.left,min,root.data) and  check_node(root.right,root.data,max)
    