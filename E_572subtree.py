from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, s, t):
        # if both tree empty
        if not s and not t:
            return True
          
        # repeat for left and right subtree
        if s and t and s.val == t.val:
            return (self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right))
        # either one is empty while another is not
        return False

    def isSubtree(self, root: List[TreeNode], subRoot: List[TreeNode]) -> bool:
        # if subTree is null
        if not subRoot: return True

        # if tree is null but subtree is not null
        if not root: return False

        # compare
        if self.isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
