#Given an array arr and a number k. One can apply a swap operation on the array any number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . Find the minimum number of swaps required to bring all the numbers less than or equal to k together, i.e. make them a contiguous subarray.
class Solution:
    def minSwap(self, arr, k):
        n = len(arr)

        # Count elements <= k
        good = 0
        for num in arr:
            if num <= k:
                good += 1

        # Count bad elements in first window
        bad = 0
        for i in range(good):
            if arr[i] > k:
                bad += 1

        ans = bad

        # Slide the window
        i = 0
        j = good

        while j < n:
            if arr[i] > k:
                bad -= 1
            if arr[j] > k:
                bad += 1

            ans = min(ans, bad)

            i += 1
            j += 1

        return ans
