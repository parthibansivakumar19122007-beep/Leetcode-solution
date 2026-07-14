# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        s=[]
        def post(node):
            if node is None:
                return
            post(node.left)
            post(node.right)
            s.append(node.val)
        post(root)
        return s