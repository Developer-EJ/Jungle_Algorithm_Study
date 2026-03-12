# 백트래킹 - Word Search
# 문제 링크: https://leetcode.com/problems/word-search/description/?envType=study-plan-v2&envId=top-interview-150


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        width = len(board[0])
        height = len(board)

        def back(x, y, index):
            if board[x][y] == "@":
                return False
            if word[index] != board[x][y]:
                return False
            if index == len(word) - 1:
                return True

            temp = board[x][y]
            board[x][y] = "@"
            for i in range(4):
                if i == 0 and y < width - 1:
                    if back(x, y + 1, index + 1):
                        return True
                elif i == 1 and y > 0:
                    if back(x, y - 1, index + 1):
                        return True
                elif i == 2 and x < height - 1:
                    if back(x + 1, y, index + 1):
                        return True
                elif i == 3 and x > 0:
                    if back(x - 1, y, index + 1):
                        return True
            board[x][y] = temp
            return False

        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    if back(i, j, 0):
                        return True
        return False
