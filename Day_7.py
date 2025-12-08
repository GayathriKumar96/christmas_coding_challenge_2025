"""
Question from  LeetCode:

169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.

"""

# Solution in Python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_nums = Counter(nums)
        n = len(nums)
        max = n//2
        max_key = -1
        for k,v in count_nums.items():
            if v>=max:
                max = v
                max_key = k
        return max_key
