class Solution:
    def divide(self, dividend: int, divisor: int):
        if divisor == dividend:
            return 1
        if dividend > divisor:
            remainder = dividend - divisor
            counter = 0
            while (remainder > divisor):
                remainder -= divisor
                counter += 1
        else:
            return 0
        return -(counter + 1) if (dividend > divisor and divisor < 0) else (counter + 1)
        

solution = Solution()
ans = solution.divide(7, -3)
print(ans)
