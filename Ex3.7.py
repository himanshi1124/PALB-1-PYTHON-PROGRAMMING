#Given a row-wise sorted matrix mat[][] of size n*m, where the number of rows and columns is always odd. Return the median of the matrix.
import bisect

class Solution:
    def median(self, mat):
        r = len(mat)
        c = len(mat[0])

        # Find min and max in matrix
        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)

        desired = (r * c) // 2

        while low < high:
            mid = (low + high) // 2

            # Count numbers <= mid
            count = 0
            for row in mat:
                count += bisect.bisect_right(row, mid)

            if count <= desired:
                low = mid + 1
            else:
                high = mid

        return low
