class Solution:
    def isPalindrome(self, s: str) -> bool: 
        proper_string = ""
        for index, char in enumerate(s):
            if char.isalnum():
                proper_string += char

        s = proper_string.lower()
        
        size, counter_y = len(s), len(s)-1
        counter_x = 0

        if size == 0  or size == 1:
            return True
        while counter_x < size:
            a = s[counter_x]
            b = s[counter_y]
            print(a, b)
            
            if a != b:
                return False
            counter_x += 1
            counter_y -= 1
        return True 

solution = Solution()
TEST_STR = "0P"
ans = solution.isPalindrome(TEST_STR)
print(str(ans))
