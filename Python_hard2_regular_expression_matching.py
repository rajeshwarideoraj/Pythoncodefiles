class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        
        # Initialize a 2D dp array with all elements as False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Handle patterns with '*'
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        # Fill the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s_char, p_char = s[i - 1], p[j - 1]

                if s_char == p_char or p_char == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p_char == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s_char == p[j - 2] or p[j - 2] == '.'))
                    
        return dp[m][n]
        