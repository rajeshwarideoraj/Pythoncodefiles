class Solution(object):
    def isPalindrome(self, x):
        # Convert the integer to a string
        str_x = str(x)
        
        # Use two pointers to compare characters from the beginning and end of the string
        left, right = 0, len(str_x) - 1
        
        while left < right:
            # If characters don't match, it's not a palindrome
            if str_x[left] != str_x[right]:
                return False
            
            # Move the pointers towards each other
            left += 1
            right -= 1
        
        # If the loop completes, it means the integer is a palindrome
        return True
        