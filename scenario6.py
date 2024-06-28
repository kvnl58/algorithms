from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        same_left = True
        same_right = True 
        same_left = self.isSameTree(p.left, q.left)
        same_right = self.isSameTree(p.right, q.right)


        return same_left and same_right


p2 = TreeNode(2)
p3 = TreeNode(3)
p1 = TreeNode(1, p2, p3)

q2 = TreeNode(2)
q3 = TreeNode(3)
q1 = TreeNode(1, q2, q3)

tree = Solution()
same = tree.isSameTree(p1, q1)
print(f"{same}")
