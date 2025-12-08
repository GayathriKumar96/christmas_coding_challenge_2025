"""
Question from  LeetCode:

1189. Maximum number of balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.


"""

# Solution in Python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text)<7:
            return 0
        text_count = Counter(text)
        balloon_count = Counter("balloon")
        c = 0
        f = 0
        while f==0:
            for x,y in balloon_count.items():
                text_count[x] -= balloon_count[x]
                if text_count[x] < 0:
                    f = 1
                    break
            if f==0:
                c+=1
        return c
