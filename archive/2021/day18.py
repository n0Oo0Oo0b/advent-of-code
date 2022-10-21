from itertools import permutations


class Node:  # Went all-out on the OOP here
    def __init__(self, s, parent=None):
        self.value = self.left = self.right = None
        self.hasValue = False
        self.parent = parent
        
        if type(s) is int or s[0] != '[':
            self.value, self.hasValue = int(s), True
            return
        
        sub = s[1:-1]
        depth = 1
        if '[' in sub:  #
            for i, char in enumerate(sub[1:]):
                if char == '[':
                    depth += 1
                elif char == ']':
                    depth -= 1
                if depth == 0:
                    self.left = Node(sub[:i+2], self)
                    self.right = Node(sub[i+3:], self)
                    return
        left, right = sub.split(',', 1)
        self.left = Node(left, self)
        self.right = Node(right, self)

    def __str__(self):
        return str(self.value) if self.hasValue else f"[{self.left},{self.right}]"
    
    def __add__(self, other):
        # Add snailfish numbers in the order a + b = [a, b]
        (n := Node(f"[{self},{other}]")).reduce()
        return n
    
    def __abs__(self):
        # Returns the magnitude of the number
        t = 0
        for child, m in zip((self.left, self.right), (3, 2)):
            if not child.hasValue:
                t += m * abs(child)
            else:
                t += m * child.value
        
        return t
    
    def rightmost(self) -> object:
        """
        Finds rightmost node from current node
        :return: Node object of rightmost node
        """
        if not self.right:
            return self
        r = self.right
        while r.right:
            r = r.right
        return r
    
    def leftmost(self) -> object:
        """
        Finds leftmost node from current node
        :return: Node object of leftmost node
        """
        if not self.left:
            return self
        l = self.left
        while l.left:
            l = l.left
        return l
    
    def previous(self, root) -> object | None:
        """
        Gets the previous node in the tree
        :param root: Root node
        :return: node of previous node
        """
        if root.leftmost() is self:  # Already rightmost node
            return None
        
        # Go up until there is right child node
        prev, p = self, self.parent
        while p.left is prev:
            prev, p = p, p.parent
        return p.left.rightmost()
    
    def next(self, root) -> object | None:
        """
        Gets the next node in the tree
        :param root: Root node
        :return: node of next node
        """
        if root.rightmost() is self:  # Already rightmost node
            return None
        
        # Go up until there is right child node
        prev, p = self, self.parent
        while p.right is prev:
            prev, p = p, p.parent
        return p.right.leftmost()
    
    def findExplosion(self, depth: int = 0) -> object | None:
        """
        Finds first node at depth >= 4 with children nodes (depth-first search)
        :param depth: Depth of the node relative to root node
        :return: Found node or None if no nodes match the criteria
        """
        if depth >= 4 and not self.hasValue:  # Node (w/ child nodes) at depth >= 4
            return self
        
        if self.left:  # Find potential explosions on left (left -> right priority)
            left = self.left.findExplosion(depth + 1)
            if left:
                return left
        
        if self.right:  # Find potential explosions on right
            right = self.right.findExplosion(depth + 1)
            if right:
                return right
    
    def explode(self) -> bool:
        """
        Explodes first node that meets the criteria (if any)
        :return bool: Whether a node was exploded
        """
        pair = self.findExplosion()
        if not pair:
            return False
        
        if left := pair.left.previous(self):
            left.value += pair.left.value
        
        if right := pair.right.next(self):
            right.value += pair.right.value
        
        pair.left = pair.right = None
        pair.value = 0
        pair.hasValue = True
        
        return True
    
    def findSplits(self, root) -> object | None:
        """
        Finds first node with value >= 10 (depth-first search)
        :param root: Root node
        :return: Found node or None if no nodes match the criteria
        """
        if self.hasValue:  # Has value
            return self if self.value >= 10 else None
        
        left = self.left.findSplits(root)  # Left side
        if left:
            return left
        
        right = self.right.findSplits(root)  # Right side
        if right:
            return right
    
    def split(self) -> bool:
        """
        Splits first node that meets the criteria (if any)
        :return bool: Whether a node was split
        """
        if not (n := self.findSplits(self)):
            return False
        
        n.left = Node(n.value // 2, parent=n)
        n.right = Node(n.value - n.left.value, parent=n)
        n.value = None
        n.hasValue = False
        
        return True
    
    def reduce(self):
        """
        Reduce the number (through explosion + split)
        :return: None
        """
        while True:
            if not self.explode() and not self.split():
                return


# Puzzle input
with open('inputs/day18.txt') as file:
    lines = [Node(i) for i in file.read().splitlines()]

# Part 1
n = lines[0]
for line in lines[1:]:
    n += line
# Part 2
m = 0
for line1, line2 in permutations(lines, 2):
    m = max(abs(line1 + line2), m)


# Output
print(f'Part 1: {abs(n)}\nPart 2: {m}')
