#Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Traverse(self, root, res):
        if root:
            self.Traverse(root.left, res)
            res.append(root.val)
            self.Traverse(root.right, res)
        
        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.Traverse(root, [])