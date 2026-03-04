class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        o = x
        a1 = 0
        while x > 0:
            a1 = a1*10+ x%10
            x = x//10
        if a1 == o:
            return True
        else :
            return False         
