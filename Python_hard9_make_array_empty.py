class Solution(object):
    def countOperationsToEmptyArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        sorted_nums = sorted(nums)
        min_index = 0
        operations = 0

        for num in nums:
            if num == sorted_nums[min_index]:
                min_index += 1
            else:
                operations += 1

        return operations
        