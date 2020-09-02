class Solution:
    def divide(self, dividend: int, divisor: int):
        if divisor == dividend:
            return 1
        if divisor < dividend and dividend < 0:
            return 0
        if divisor == 1:
            return dividend

        d = divisor
        divisor = abs(divisor)
        if dividend > divisor:
            remainder = dividend - divisor
            counter = 0
            while (remainder > divisor):
                remainder -= divisor
                counter += 1
        else:
            return 0
        return -(counter + 1) if (dividend > d and d < 0) else (counter + 1)
        

solution = Solution()
ans = solution.divide(7, -3)
print(ans)
