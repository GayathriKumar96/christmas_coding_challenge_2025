"""
Question from  LeetCode:

14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.


"""

# Solution in Python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        main_word = strs[0]
        for i in range(len(main_word)):
            f=1
            for st in strs:
                if i<len(st):
                    if main_word[i]!=st[i]:
                        f=0
                        break
                else:
                    f=0
                    break

            if f==1:
                prefix+=main_word[i]
            else:
                break
        return prefix
