# https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=top-interview-150


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_depth = 0
        if root is None:
            return 0

        def backtrack(node, current_height):
            if node is None:
                self.max_depth = max(self.max_depth, current_height)
                return

            backtrack(node.left, current_height + 1)
            backtrack(node.right, current_height + 1)

        backtrack(root, 0)
        return self.max_depth


# 더 간단한 재귀 풀이
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
