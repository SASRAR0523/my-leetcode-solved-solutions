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

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:
# Input: n = 3 Output: ["((()))","(()())","(())()","()(())","()()()"] 
# Example 2:
# Input: n = 1 Output: ["()"]
        
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current: str, open_count: int, close_count: int) -> None:
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result

# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.
# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        longest = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    # This ')' can't be part of a valid substring.
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1])

        return longest

# A parentheses string is valid if and only if:

# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        additions = 0

        for ch in s:
            if ch == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    additions += 1

        return additions + balance

# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

 class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        depth = 0

        for ch in s:
            if ch == '(':
                depth += 1
                if depth > 1:
                    ans.append(ch)
            else:
                if depth > 1:
                    ans.append(ch)
                depth -= 1

        return ''.join(ans)

# You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.

# The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.

# You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.

# Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.

# Note: You are allowed to modify the array elements to become negative integers.

class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2

            if sum(max(0, d - mid) for d in diff) <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        remaining = k - sum(max(0, d - level) for d in diff)

        diff = [min(d, level) for d in diff]

        for i in range(len(diff)):
            if remaining == 0:
                break
            if diff[i] == level:
                diff[i] -= 1
                remaining -= 1

        return sum(d * d for d in diff)

# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, 
# you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

# Notice that you can not jump outside of the array at any time.

class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        visited = set()
        stack = [start]

        while stack:
            i = stack.pop()

            if arr[i] == 0:
                return True

            if i in visited:
                continue

            visited.add(i)

            if i + arr[i] < len(arr):
                stack.append(i + arr[i])

            if i - arr[i] >= 0:
                stack.append(i - arr[i])

        return False

# You are given a 0-indexed integer array nums and a target element target.

# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)

        return result

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# You are given an integer array nums of length n, where nums is a permutation of the numbers in the range [0..n - 1].

# You may swap elements at indices i and j only if nums[i] AND nums[j] == k, where AND denotes the bitwise AND operation and k is a non-negative integer.

# Return the maximum value of k such that the array can be sorted in non-decreasing order using any number of such swaps. If nums is already sorted, return 0.

 class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1
        
        for i, val in enumerate(nums):
            if val != i:
                if k == -1:
                    k = val
                else:
                    k &= val
        
        return 0 if k == -1 else k
