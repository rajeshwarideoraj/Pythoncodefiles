class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Helper function to check if a string represents a valid integer
        def isInteger(s):
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            return s.isdigit()

        # Helper function to check if a string represents a valid decimal
        def isDecimal(s):
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            if '.' not in s:
                return False
            integer_part, decimal_part = s.split('.')
            return (integer_part.isdigit() or integer_part == '') and decimal_part.isdigit()

        s = s.strip()  # Remove leading and trailing whitespaces

        # Check for the presence of 'e' or 'E' to determine if it's a decimal with exponent
        if 'e' in s or 'E' in s:
            base, exponent = s.split('e') if 'e' in s else s.split('E')

            # Check if both parts are either integers or decimals
            return (isInteger(base) or isDecimal(base)) and isInteger(exponent)

        # If there is no 'e' or 'E', check if it's either an integer or a decimal
        return isInteger(s) or isDecimal(s)

# Example usage:
solution = Solution()
print(solution.isNumber("2"))        # True
print(solution.isNumber("0089"))     # True
print(solution.isNumber("-0.1"))      # True
print(solution.isNumber("+3.14"))     # True
print(solution.isNumber("4."))        # True
print(solution.isNumber("-.9"))       # True
print(solution.isNumber("2e10"))      # True
print(solution.isNumber("-90E3"))     # True
print(solution.isNumber("3e+7"))      # True
print(solution.isNumber("+6e-1"))     # True
print(solution.isNumber("53.5e93"))   # True
print(solution.isNumber("-123.456e789"))  # True

print(solution.isNumber("abc"))       # False
print(solution.isNumber("1a"))        # False
print(solution.isNumber("1e"))        # False
print(solution.isNumber("e3"))        # False
print(solution.isNumber("99e2.5"))    # False
print(solution.isNumber("--6"))       # False
print(solution.isNumber("-+3"))       # False
print(solution.isNumber("95a54e53"))  # False
        