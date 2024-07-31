# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeaves(root1, []) == self.getLeaves(root2, [])
        
    def getLeaves(self, root, leaves):
        if not root:
            return

        if not root.left and not root.right: #leaf node
            leaves.append(root.val)

        self.getLeaves(root.left, leaves)
        self.getLeaves(root.right, leaves)

        return leaves
