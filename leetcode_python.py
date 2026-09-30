# 1. Concatenation of Array

# Given an integer array nums of length n, you want to create an array ans of length 2n 
# where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

class Solution:
    def getConcatenation(self, nums):
        return nums + nums

# 2. Smallest Stable Index 2

# You are given an integer array nums of length n and an integer k.

# For each index i, define its instability score as max(nums[0..i]) - min(nums[i..n - 1]).

# In other words:

# max(nums[0..i]) is the largest value among the elements from index 0 to index i.
# min(nums[i..n - 1]) is the smallest value among the elements from index i to index n - 1.
# An index i is called stable if its instability score is less than or equal to k.

# Return the smallest stable index. If no such index exists, return -1

class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)

        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        prefix_max = nums[0]

        for i in range(n):
            prefix_max = max(prefix_max, nums[i])

            if prefix_max - suffix_min[i] <= k:
                return i

        return -1

# 3. Distinct Subsequences

# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.

class Solution:
    def numDistinct(self, s, t):
        m = len(s)
        n = len(t)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Empty string can be formed in one way
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]
# Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at x = i, find the number of ways
# we can draw exactly k non-overlapping line segments such that each segment covers two or more points.
# The endpoints of each segment must have integral coordinates. The k line segments do not have to cover all n points,
# and they are allowed to share endpoints.

# Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 109 + 7.
        
class Solution:    
    def numberOfSets(self, n, k):        
        MOD = 10**9 + 7        
        
        N = n + k - 1        
        r = 2 * k        
        ans = 1        
        for i in range(1, r + 1):            
            ans = ans * (N - r + i) // i

# You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.

# For example, in the string "(name)is(age)yearsold", there are two bracket pairs that contain the keys "name" and "age".
# You know the values of a wide range of keys. This is represented by a 2D string array knowledge where 
# each knowledge[i] = [keyi, valuei] indicates that key keyi has a value of valuei.

# You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains some key keyi, you will:

# Replace keyi and the bracket pair with the key's corresponding valuei.
# If you do not know the value of the key, you will replace keyi and the bracket pair with a question mark "?" (without the quotation marks).
# Each key will appear at most once in your knowledge. There will not be any nested brackets in s.

# Return the resulting string after evaluating all of the bracket pairs.
 class Solution:
    def evaluate(self, s, knowledge):
        mp = dict(knowledge)
        ans = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i + 1:j]
                ans.append(mp.get(key, '?'))
                i = j + 1
            else:
                ans.append(s[i])
                i += 1

        return ''.join(ans)     

# You are given a string s that consists of lower case English letters and brackets.

# Reverse the strings in each pair of matching parentheses, starting from the innermost one.

# Your result should not contain any brackets.

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == ')':
                temp = []

                while stack[-1] != '(':
                    temp.append(stack.pop())

                stack.pop()  # remove '('

                stack.extend(temp)

            elif ch == '(':
                stack.append(ch)

            else:
                stack.append(ch)

        return ''.join(stack)

# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

# Example 1:

# Input: s = "(1+(2*3)+((8)/4))+1"

# Output: 3

# Explanation:

# Digit 8 is inside of 3 nested parentheses in the string.

class Solution:
    def maxDepth(self, s):
        depth = 0
        ans = 0

        for ch in s:
            if ch == '(':
                depth += 1
                ans = max(ans, depth)
            elif ch == ')':
                depth -= 1

        return ans

# You are given an integer array nums.

# Return the smallest index i such that the sum of the digits of nums[i] is equal to i.

# If no such index exists, return -1.

class Solution:
    def smallestIndex(self, nums):
        for i, num in enumerate(nums):
            if sum(map(int, str(num))) == i:
                return i
        return -1

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
# that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution:
    def letterCombinations(self, digits):
        mp = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        ans = []

        def backtrack(i, cur):
            if i == len(digits):
                ans.append(cur)
                return

            for ch in mp[digits[i]]:
                backtrack(i + 1, cur + ch)

        backtrack(0, "")
        return ans
        
        
