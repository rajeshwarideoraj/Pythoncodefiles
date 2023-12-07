class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a mapping of Roman numerals to their corresponding values
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = 0

        # Iterate through the string from left to right
        for i in range(len(s)):
            # Get the value of the current Roman numeral
            current_numeral = roman_map[s[i]]

            # Check if we need to subtract the previous numeral
            if i > 0 and current_numeral > roman_map[s[i - 1]]:
                result += current_numeral - 2 * roman_map[s[i - 1]]
            else:
                result += current_numeral

        return result

# Example usage:
solution = Solution()
print(solution.romanToInt("III"))  # Output: 3
print(solution.romanToInt("IV"))   # Output: 4
print(solution.romanToInt("IX"))   # Output: 9
print(solution.romanToInt("LVIII")) # Output: 58
print(solution.romanToInt("MCMXCIV")) # Output: 1994