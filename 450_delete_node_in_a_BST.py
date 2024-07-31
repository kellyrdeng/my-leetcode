# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.val == key: #delete and preserve binary property
            if not root.left and not root.right: #leaf node
                return None

            if not root.left:
                return root.right

            if not root.right:
                return root.left

            if root.left and root.right: #return the smallest child of root.right
                #find new root
                curr = root.right
                while curr.left:
                    curr = curr.left

                root.val = curr.val

                #delete curr from the right subtree
                root.right = self.deleteNode(root.right, curr.val)

        if key < root.val: #if key is in left subtree, recurse on it to delete it
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root
