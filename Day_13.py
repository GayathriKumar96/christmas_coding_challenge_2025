"""
Question from  LeetCode:

54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]


Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100


"""

# Solution in Python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        if m==1 and n==1:
            return [matrix[0][0]]
        if m==1 and n>1:
            return matrix[0][:]
        if n==1 and m>1:
            return [matrix[i][0] for i in range(m)]
        
        result = []
        up_wall = 1
        down_wall = m-1
        left_wall = 0
        right_wall = n-1
        i = 0
        j = 0
        while len(result) < m*n:
            while j <= right_wall:
                result.append(matrix[i][j])
                if len(result) == m*n:
                    break
                j+=1
            if len(result) == m*n:
                break
            right_wall -= 1
            j -= 1
            i += 1
            while i <= down_wall:
                result.append(matrix[i][j])
                if len(result) == m*n:
                    break
                i+=1
            down_wall -= 1
            i -= 1
            j -= 1
            while j>=left_wall:
                result.append(matrix[i][j])
                if len(result) == m*n:
                    break
                j-=1
            left_wall += 1
            j += 1
            i -= 1
            while i>=up_wall:
                result.append(matrix[i][j])
                if len(result) == m*n:
                    break
                i-=1
            up_wall += 1
            i+=1
            j+=1

        return result
        
     
