class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 2:
            return s

        n = len(s)
        start = 0  # Start index of the longest palindromic substring
        max_len = 1  # Length of the longest palindromic substring

        # Function to expand around the center and find palindrome
        def expand_around_center(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(n):
            len1 = expand_around_center(i, i)  # Odd length palindrome
            len2 = expand_around_center(i, i + 1)  # Even length palindrome

            # Find the maximum length palindrome centered at i
            curr_max_len = max(len1, len2)

            if curr_max_len > max_len:
                max_len = curr_max_len
                start = i - (curr_max_len - 1) // 2

        return s[start:start + max_len]
        