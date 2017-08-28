class New_Node(object):
    __slots__ = ['num', 'children']

    def __init__(self):
        self.num = 0
        self.children = {}
        
class Trie(object):
        def __init__(self):
            self.root = New_Node()

        def add(self,word):
            current_node = self.root
            for char in word:
                if char in current_node.children:
                    current_node = current_node.children[char]
                else:
                    current_node.children[char] = New_Node()
                    current_node = current_node.children[char]
                current_node.num += 1

        def find(self,partial):
            current_node = self.root
            for char in partial:
                if char not in current_node.children:
                    return 0
                current_node = current_node.children[char]
            return current_node.num

if __name__ == "__main__":
    n = int(raw_input().strip())
    trie = Trie()
    for _ in xrange(n):
        op, contact = raw_input().strip().split(' ')
        if op == 'add':
            trie.add(contact)
        elif op == 'find':
            print trie.find(contact)