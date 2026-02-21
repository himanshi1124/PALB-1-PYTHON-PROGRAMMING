#You are given a rectangular matrix mat[][] of size n x m, and your task is to return an array while traversing the matrix in spiral form.
class Solution:
    def spirallyTraverse(self, mat):
        result = []

        if not mat:
            return result

        top = 0
        bottom = len(mat) - 1
        left = 0
        right = len(mat[0]) - 1

        while top <= bottom and left <= right:

            # Left → Right
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1

            # Top → Bottom
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1

            # Right → Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1

            # Bottom → Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1

        return result
