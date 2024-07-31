# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recurse down every path
# keep track of path for each recursion (OR MAX?????)
# keep a goodNodes var and update it for each node by comparing to max

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = []
        self.helper(goodNodes, root.val, root)
        return len(goodNodes)
        
    def helper(self, goodNodes, maxi, root):
        if not root:
            return None

        if root.val >= maxi: #goodNode
            goodNodes.append(root.val)
            maxi = root.val

        self.helper(goodNodes, maxi, root.left)
        self.helper(goodNodes, maxi, root.right)
