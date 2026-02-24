# You are given a rectangular matrix mat[][] of size n x m, and your task is to return an array while traversing the matrix in spiral form.

class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        if not mat or not mat[0]:
            return []
            
        # Initialize boundaries
        rows = len(mat)
        cols = len(mat[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        
        result = []
        
        # Loop until boundaries overlap
        while top <= bottom and left <= right:
            # 1. Move from Left to Right along the 'top' row
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1 # Shrink top boundary
            
            # 2. Move from Top to Bottom along the 'right' column
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1 # Shrink right boundary
            
            # 3. Move from Right to Left along the 'bottom' row
            # Check if there is still a row to traverse
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1 # Shrink bottom boundary
                
            # 4. Move from Bottom to Top along the 'left' column
            # Check if there is still a column to traverse
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1 # Shrink left boundary
                
        return result
