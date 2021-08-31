# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inTr(root)
        return self.ans
        
    def inTr(self, root: Optional[TreeNode]):
        if root:
            self.inTr(root.left)
            self.ans.append(root.val)
            self.inTr(root.right)
        
