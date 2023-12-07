class Solution(object):
    def countAnagrams(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7

        # Step 1: Split the input string into an array of words
        words = s.split()

        # Step 2: Count the occurrences of each character in each word
        # Step 3: Use a dictionary to store the frequency of each word's signature
        signature_count = {}
        for word in words:
            signature = ''.join(sorted(word))
            signature_count[signature] = signature_count.get(signature, 0) + 1

        # Step 4: Calculate the total number of distinct anagrams
        result = 1
        for count in signature_count.values():
            # Use modular arithmetic to avoid overflow
            result = (result * self.factorial(count)) % MOD

        return result

    # Helper function to calculate the factorial of a number
    def factorial(self, n):
        result = 1
        for i in range(2, n + 1):
            result = (result * i) % (10**9 + 7)
        return result
        