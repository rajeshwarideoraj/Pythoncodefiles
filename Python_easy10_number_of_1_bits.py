class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        
        # Iterate through each bit
        while n != 0:
            count += n & 1  # Check the rightmost bit
            n = n >> 1     # Right shift the bits
            
        return count
        