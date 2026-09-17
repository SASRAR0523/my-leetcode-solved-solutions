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

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside 
# the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).      






