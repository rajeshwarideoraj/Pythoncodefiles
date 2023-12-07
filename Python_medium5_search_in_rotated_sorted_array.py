class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            # Check if the left half is sorted
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    # Target is in the left half
                    right = mid - 1
                else:
                    # Target is in the right half
                    left = mid + 1
            elif nums[left] > nums[mid]:
                # Check if the right half is sorted
                if nums[mid] < target <= nums[right]:
                    # Target is in the right half
                    left = mid + 1
                else:
                    # Target is in the left half
                    right = mid - 1
            else:
                # Handle the case where nums[left] == nums[mid]
                left += 1

        return False
        