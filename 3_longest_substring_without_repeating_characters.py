"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        start = 0
        max_length = 0

        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1

            char_index[s[end]] = end

            max_length = max(max_length, end - start + 1)
        return max_length

solution = Solution()

cases = [
    {"s": "abcabcbb", "expected": 3},
    {"s": "bbbbb", "expected": 1},
    {"s": "pwwkew", "expected": 3},
]

for case in cases:
    assert solution.lengthOfLongestSubstring(s=case["s"]) == case["expected"]

print("Longest substring successfull!")