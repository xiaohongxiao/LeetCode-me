class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)
        result = 0
        while x:
            result = result*10 + x % 10
            x = x // 10
        if result <= 0x7fffffff:
            return result
        else:
            return 0