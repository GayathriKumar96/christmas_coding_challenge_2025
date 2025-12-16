"""
Question from  LeetCode:

56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""

# Solution in Python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        merged_intervals = []
        merged_ind = -1
        if intervals[1][0]-intervals[0][1] < 1:
            if intervals[1][1]<=intervals[0][1]:
                merged_intervals.append(intervals[0])
            else:
                merged_intervals.append([intervals[0][0],intervals[1][1]])
            merged_ind = 0
        else:
            merged_intervals = intervals[0:2]
            merged_ind = 1
        
        for i in range(2,len(intervals)):
            if intervals[i][0] - merged_intervals[merged_ind][1] < 1:
                if intervals[i][1]<=merged_intervals[merged_ind][1]:
                    merged_intervals.append(merged_intervals[merged_ind])
                else:
                    merged_intervals.append([merged_intervals[merged_ind][0],intervals[i][1]])
                del(merged_intervals[merged_ind])
            else:
                merged_intervals.append(intervals[i])
                merged_ind += 1
        return merged_intervals
