class Solution(object):
    def removeDuplicates(self, nums):
        # Check for edge cases
        if not nums:
            return 0

        # Initialize a pointer for unique elements
        unique_pointer = 0

        # Iterate through the array
        for i in range(1, len(nums)):
            # If the current element is different from the previous one, update the pointer and update the array
            if nums[i] != nums[unique_pointer]:
                unique_pointer += 1
                nums[unique_pointer] = nums[i]

        # Return the number of unique elements
        return unique_pointer + 1

# Example usage:
# nums = [1, 1, 2, 2, 3, 4, 4, 5]
# solution = Solution()
# k = solution.removeDuplicates(nums)
# print(nums[:k])
# Output: [1, 2, 3, 4, 5]
        