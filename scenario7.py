from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        root = None

    def create_tree(self, root_arr):
        if not root_arr:
            return None

        self.root = TreeNode(root_arr[0])
        q = [self.root]
        i = 1
        while i < len(root_arr):
            curr = q.pop(0)
            if i < len(root_arr):
                curr.left = TreeNode(root_arr[i])
                q.append(curr.left)
                i += 1
            if i < len(root_arr):
                curr.right = TreeNode(root_arr[i])
                q.append(curr.right)
                i += 1

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = root
        def dfs(start, p, q):
            if not start:
                return False, False
            found_p = False
            found_q = False

            if start == p:
                found_p = True
            if start == q:
                found_q = True

            left_p, left_q = dfs(start.left, p, q)
            right_p, right_q = dfs(start.right, p, q)

            found_p = found_p or left_p or right_p
            found_q = found_q or left_q or right_q

            if found_p and found_q:
                nonlocal ancestor
                ancestor = start
                return False, False

            return found_p, found_q

        dfs(root, p, q)
        return ancestor

    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        out = []
        frontier = deque()
        frontier.append((0, root))

        while frontier:
            curr_level, curr_node = frontier.popleft()
            
            if curr_node.left:
                frontier.append((curr_level + 1, curr_node.left))
            if curr_node.right:
                frontier.append((curr_level + 1, curr_node.right))

            if len(out) <= curr_level:
                out.append([])
            out[curr_level].append(curr_node.val)

        return out

    def maxPathSum(self, root):
        out = float('-inf')
        def maxPathS(start):
            if not start:
                return 0
            left = maxPathS(start.left)
            right = maxPathS(start.right)

            maxPath = max(left + start.val, right + start.val)
            through = left + right + start.val

            nonlocal out
            if through > out:
                out = through
            if maxPath > out:
                out = maxPath

            return maxPath
        maxPathS(root)
        return out 
        

sol = Solution()
#arr = [5,3,8,1,4,7,9, None, 2]
#arr = [3,9,20,None, None, 15,7]
arr = [2,-1,-2]
#sol.create_tree(arr)
#ancestor = sol.lowestCommonAncestor(sol.root, sol.root.left, sol.root.left.right)
#print(f"{ancestor.val}")
#trav = sol.levelOrder(sol.root)
#print(f"{trav}")

sol.create_tree(arr)
sum = sol.maxPathSum(sol.root)

print(f"max path sum: {sum}")


