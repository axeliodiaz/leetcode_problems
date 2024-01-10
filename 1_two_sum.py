"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for pos, i in enumerate(nums):
            for pos2, j in enumerate(nums):
                if nums[pos] + nums[pos2] == target and not pos == pos2:
                    return [pos, pos2]


solution = Solution()
cases = [
    {"nums": [2,7,11,15], "target": 9, "expected": [0,1]},
    {"nums": [3,2,4], "target": 6, "expected": [1,2]},
    {"nums": [3,3], "target": 6, "expected": [0,1]},
]
for case in cases:
    assert solution.twoSum(nums=case["nums"], target=case["target"]) == case["expected"]

print("Two sums successful!")
