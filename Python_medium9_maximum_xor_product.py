class Solution(object):
    def maximumXorProduct(self, a, b, n):
        """
        :type a: int
        :type b: int
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        max_product = 0

        for x in range(1 << n):
            xor_a = a ^ x
            xor_b = b ^ x
            product = (xor_a % MOD) * (xor_b % MOD) % MOD
            max_product = max(max_product, product)

        return max_product
        