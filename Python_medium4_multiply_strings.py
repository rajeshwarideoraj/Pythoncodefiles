class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Multiply each digit and add to the result
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                total_sum = mul + result[i + j + 1]
                result[i + j + 1] = total_sum % 10
                result[i + j] += total_sum // 10

        # Convert the result list to a string
        result_str = ''.join(map(str, result)).lstrip('0')

        return result_str if result_str else '0'