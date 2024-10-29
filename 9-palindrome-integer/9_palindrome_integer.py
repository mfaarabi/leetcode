import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if 0 <= x < 10:
            return True
        if x < 0:
            return False

        numFromRight = x

        numFromLeft = x
        # i.e. if a number is between 100 and 1000,
        # log10 value will be decimal between 2 and 3.
        # hence the floor since we just want the 2.
        divisor = 10 ** math.floor(math.log10(numFromLeft))
        
        while numFromRight > 0 and divisor > 0:
            if numFromRight % 10 != numFromLeft // divisor:
                return False

            numFromRight //= 10

            numFromLeft %= divisor
            divisor //= 10
        
        return True