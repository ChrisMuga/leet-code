class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = 0
        count = 0
        max_count = 0
        char_set = set()
        for x in range(len(s)):
            for char_y in s[index:]:
                if char_y in char_set:
                    char_set = set()
                    break
                else:
                    char_set.add(char_y)
                    count += 1
                    max_count = max(count, max_count)
            count = 0
            index += 1
        return max_count


solution = Solution()
print(solution.lengthOfLongestSubstring("dvdf"))
# print(solution.lengthOfLongestSubstring("asjrgapa"))

