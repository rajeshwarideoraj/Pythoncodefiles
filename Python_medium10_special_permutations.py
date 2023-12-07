class Solution(object):
    def specialPerm(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Sort the array to simplify the counting process
        nums.sort()

        # dp[i] represents the number of special permutations ending with nums[i]
        dp = [1] * n

        # Iterate over each element in the array
        for i in range(1, n):
            # For each element, check its divisibility with previous elements
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    # If divisible, update dp[i] by adding dp[j]
                    dp[i] = (dp[i] + dp[j]) % MOD

        # Sum up all the values in dp array to get the total number of special permutations
        result = sum(dp) % MOD

        return result
        