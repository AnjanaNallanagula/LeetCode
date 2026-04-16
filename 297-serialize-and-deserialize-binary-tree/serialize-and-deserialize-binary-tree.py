from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        s = ""
        q = deque([])
        q.append(root)

        while (len(q) != 0):
            node = q.popleft()

            if (node != None):
                s += "," + str(node.val)

                q.append(node.left)
                q.append(node.right)
            else:
                s += "," + "-1001"
        
        return s
                
    def deserialize(self, data):
        if (data == ",-1001"):
            return None
        
        ls = data.split(",")
        ls = ls[1:]
        q = deque([])
        root = TreeNode(int(ls[0]))
        q.append(root)
        i = 1

        while (len(q) != 0):
            node = q.popleft()

            if (i < len(ls) and ls[i] != "-1001"):
                node.left = TreeNode(int(ls[i]))
                q.append(node.left)
                
            i += 1

            if (i < len(ls) and ls[i] != "-1001"):
                node.right = TreeNode(int(ls[i]))
                q.append(node.right)
                
            i += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))