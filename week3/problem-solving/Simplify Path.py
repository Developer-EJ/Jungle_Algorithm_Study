# https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150
# 경로 단순화


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        split_path = path.split("/")
        stack = []
        for ch in split_path:
            if ch == "" or ch == ".":
                continue

            if ch == "..":
                if len(stack) > 0:
                    stack.pop()
                    continue
                else:
                    continue

            stack.append(ch)
        return "/" + "/".join(stack)
