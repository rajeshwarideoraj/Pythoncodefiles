class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        result = 0

        for l in range(n):
            cnt = 0

            for r in range(l, n):
                if nums[r] % modulo == k:
                    cnt += 1

                if cnt % modulo == k:
                    result += 1

        return result

        