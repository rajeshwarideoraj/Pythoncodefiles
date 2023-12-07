class Solution(object):
    def twoSum(self, nums, target):
        # Create a dictionary to store the difference between target and each element
        complement_dict = {}

        # Iterate through the array
        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in complement_dict:
                # If found, return the indices of the two numbers
                return [complement_dict[complement], i]

            # If complement is not found, add the current number and its index to the dictionary
            complement_dict[num] = i

        # If no solution is found, return an empty list
        return []
        