# Regular BST implementation, from which AVL is derived (use the AVL class
# instead of this one in your code).
class BST(object):
    """
    Simple binary search tree implementation.
    This BST supports insert, find, and delete-min operations.
    Each tree contains some (possibly 0) BSTnode objects, representing nodes,
    and a pointer to the root.
    """

    def __init__(self):
        self.root = None

    def insert(self, t):
        """Insert key t into this BST, modifying it in-place."""
        new = BSTnode(t)
        # Empty tree case
        if self.root is None:
            self.root = new
        # Otherwise, branch down the tree until we find an empty branch
        # where we can place the new node
        else:
            node = self.root
            while True:
                if overlap(node.key, t):
                    break
                if t < node.key:
                    # Go left
                    if node.left is None:
                        node.left = new
                        new.parent = node
                        break
                    node = node.left
                else:
                    # Go right
                    if node.right is None:
                        node.right = new
                        new.parent = node
                        break
                    node = node.right
        return new

    def find(self, t):
        """Return the node for key t if is in the tree, or None otherwise."""
        node = self.root
        while node is not None:
            if t == node.key:
                return node
            elif t < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def delete(self, node):
        """Delete the given node."""
        if node.left == None:
            if node == self.root:
                self.root = node.right
                if node.right:
                    node.right.parent = None
            elif node.parent.left == node:
                node.parent.left = node.right
                if node.right:
                    node.right.parent = node.parent
            else:
                node.parent.right = node.right
                if node.right:
                    node.right.parent = node.parent
        elif node.right == None:
            if node == self.root:
                self.root = node.left
                node.left.parent = None
            elif node.parent.left == node:
                node.parent.left = node.left
                node.left.parent = node.parent
            else:
                node.parent.right = node.left
                node.left.parent = node.parent
        else:
            # Create a BST rooted at the right node
            new_bst = BST()
            new_bst.root = node.right
            node.right.parent = None

            smallest, _ = new_bst.delete_min()
            if node == self.root:
                self.root = smallest
            elif node.parent.left == node:
                node.parent.left = smallest
                smallest.parent = node.parent
            else:
                node.parent.right = smallest
                smallest.parent = node.parent
            smallest.left = node.left
            smallest.right = new_bst.root
            if smallest.left:
                smallest.left.parent = smallest
            if smallest.right:
                smallest.right.parent = smallest
        node.disconnect()

    def delete_min(self):
        """Delete the minimum key (and return the old node containing it)."""
        if self.root is None:
            return None, None
        else:
            # Walk to leftmost node.
            node = self.root
            while node.left is not None:
                node = node.left
            # Remove that node and promote its right subtree.
            if node.parent is not None:
                node.parent.left = node.right
            else: # The root was smallest.
                self.root = node.right
            if node.right is not None:
                node.right.parent = node.parent
            parent = node.parent
            node.disconnect()
            return node, parent

    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])

class BSTnode(object):
    """
    Representation of a node in a binary search tree.
    Has a left child, right child, and key value.
    """
    def __init__(self, t):
        """Create a new leaf with key t."""
        self.key = t
        self.disconnect()
    def disconnect(self):
        self.left = None
        self.right = None
        self.parent = None

def height(node):
    if node is None:
        return -1
    else:
        return node.height

def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1

def overlap(key, t):
    nodeMin = key[0]
    nodeMax = key[1]
    tMin = t[0]
    tMax = t[1]
    if nodeMax < tMin:
        return False
    elif tMax < nodeMin:
        return False
    return True

class AVL(BST):
    """
    AVL binary search tree implementation.
    Supports insert, find, and delete-min operations in O(lg n) time.
    """
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)

    def insert(self, t, type2):
        """Insert key t into this tree, modifying it in-place."""
        node = BST.insert(self, t)
        node.type = type2
        self.rebalance(node)
        # print self

    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    def delete(self, node):
        parent = node.parent
        if self.root == node:
            root = True
        else:
            root = False
            if parent.left == node:
                left = True
            else:
                left = False
        BST.delete(self, node)
        # Update the height of the node that is now where node used to be
        # since it's possible we pulled up the min of the right subtree
        if root:
            if self.root:
                update_height(self.root)
        elif left and parent.left:
            update_height(parent.left)
        elif not left and parent.right:
            update_height(parent.right)

        self.rebalance(parent)

    def delete_min(self):
        node, parent = BST.delete_min(self)
        self.rebalance(parent)

    def find(self, t):
        node = self.root
        while node is not None:
            if overlap(node.key, [t, t]):
                if node.type == 'V':
                    return 'forward'
                elif node.type == 'Q':
                    return 'quarantine'
            elif [t, t] < node.key:
                node = node.left
            else:
                node = node.right
        return 'drop'

# Call this python module directly to test that the BST functions correctly.
def test(args=None, BSTtype=AVL):
    import random, sys
    if not args:
        args = sys.argv[1:]
    if not args:
        print 'usage: %s <number-of-random-items | item item item ...>' % \
              sys.argv[0]
        sys.exit()
    elif len(args) == 1:
        items = (random.randrange(100) for i in xrange(int(args[0])))
    else:
        items = [int(i) for i in args]

    tree = BSTtype()
    print tree
    for item in items:
        print
        print 'Inserting', item
        tree.insert(item)
        print tree

if __name__ == '__main__': test()

# DO NOT MODIFY THIS FUNCTION. It is used by the grader to pass in streams of
# packets to your code. Instead modify the recv_*_packet functions below.
def handle_packet_stream(packets):
  """
  Handle a list of packets. Command packets will be formatted as a tuple
  of (start, end, type). Regular packets will be a single value, indicating
  the port to which the packet is addressed. For each regular packet, if that
  port is currently marked valid, it should be added to the list of forwarded
  packets; if it is currently marked invalid, it should be added to the list of
  dropped packets; and if it is currently marked as quarantined, it should be
  added to a list of quarantined packets. All three lists are returned.
  """
  forwarded = []
  quarantine = []
  dropped = []
  for i, packet in enumerate(packets):
    # Command packet: (start, end, type)
    if type(packet) == tuple:
      recv_command_packet(*packet)
    # Regular packet: (port, answer)
    else:
      action = recv_regular_packet(packet)
      if action == 'forward':
        forwarded.append(i)
      elif action == 'quarantine':
        quarantine.append(i)
      else:
        dropped.append(i)
  return [forwarded, quarantine, dropped]

avlTree = AVL()

#
# FILL IN THE FUNCTIONS BELOW
#

# Note: The functions below will be called multiple times per test. You will
# have to maintain some global state (most likely involving a BST) to ensure
# that you don't lose information about which ranges are
# valid/invalid/quarantined. Your module will be reloaded for each test case, so
# you start with a clean state each time.
def recv_command_packet(start, end, t):
    """
    Receive a command packet, which gives some port range information. |start|
    and |end| are integers indicating the port range should be [start, end]
    (inclusive), and t is a single character. 'V' means valid, 'Q' means
    quarantined. All ports are initially invalid.
    """
    avlTree.insert([start, end], t)

def recv_regular_packet(port):
    """
    Receive a regular data packet. |port| indicates which port the packet is
    addressed to. If the port is valid, return 'forward', if the port is
    quarantined return 'quarantine', and if the port is invalid, return 'drop'.
    """
    return avlTree.find(port)
