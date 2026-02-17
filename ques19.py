#Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n. 
class Solution:
    def factorial(self, n):
        
        result = [1]   
        for num in range(2, n + 1):
            carry = 0
            
            for i in range(len(result)):
                product = result[i] * num + carry
                result[i] = product % 10
                carry = product // 10
            
            while carry:
                result.append(carry % 10)
                carry //= 10
        
        result.reverse()
        return result
