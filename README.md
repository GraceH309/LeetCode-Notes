# LeetCode Self-Practice Notes
I sorted these classic algorithm problems by category for regular review.
Every single problem contains three parts: clean Python code, short explanation, and time & space complexity analysis.

## Catalog
1. Array & String (12)
2. Linked List ()
3. Stack & Queue ()
4. Binary Tree ()
5. Binary Search & Sort ()
6. Dynamic Programming ()

---

# 1. Array & String (12)
### 1. Two Sum
#### Python Code
```python
# 踩坑：暴力双层循环大数据直接超时，哈希表一次遍历优化
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        record = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in record:
                return [record[diff], idx]
            record[num] = idx
        return []
```

```Explanation
My first brute force two-loop solution hit time limit exceeded for large input. I switched to a hash map to store numbers and their indexes. Calculate the complement needed for target each iteration, return two indexes once the complement is found in map.
```

```Complexity Analysis
Time: O (n)
Space: O (n)
哈希表最多存储全部数组元素
```

### 2. Best Time to Buy & Sell Stock
#### Python Code
```python
# 踩坑：一开始双向遍历，没必要，一次遍历维护最小值即可
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for p in prices[1:]:
            if p < min_price:
                min_price = p
            else:
                max_profit = max(max_profit, p - min_price)
        return max_profit
```

```Explanation
We can only buy before selling. Track the minimum price we’ve seen as we loop through prices. Update min price if current price is lower, otherwise calculate profit and refresh max profit.
```

```Complexity Analysis
Time: O (n)
Space: O (1)
仅两个变量存储临时数据，无额外数组
```

### 3. Contains Duplicate
#### Python Code
```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

```Explanation
Use a set to record visited numbers. If current number exists in the set, duplicate found, return True immediately. Return False after full iteration without duplicates.
```

```Complexity Analysis
Time: O(n)
Space: O(n)
```

### 4. Product of Array Except Self
#### Python Code
```python
# 题目禁止使用除法，分左右两轮前缀乘积计算
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        left = 1
        # 先填充左侧所有数字乘积
        for i in range(n):
            res[i] = left
            left *= nums[i]
        # 反向遍历，乘上右侧所有数字乘积
        right = 1
        for i in range(n-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
```

```Explanation
Use a set to record visited numbers. If current number exists in the set, duplicate found, return True immediately. Return False after full iteration without duplicates.
```

```Complexity Analysis
Time: O(n)
Space: O(n)
```

### 5. Maximum Subarray
#### Python Code
```python
# Kadane贪心算法，处理全负数边界
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
        return max_sum
```

```Explanation
Greedy Kadane algorithm: if previous subarray sum plus current value is smaller than value itself, reset current sum to current number. Keep updating global maximum sum each step.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 6. Maximum Sum Subarray
#### Python Code
```python
# 和第5题为同一道LeetCode 53，重复练习巩固Kadane算法
# 重点复盘全负数输入场景，算法不会错误取0，始终选取最大单个负数
```

```Explanation
Same problem as No.5, repeated practice to consolidate Kadane algorithm, focus on all-negative edge case.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 7. Valid Anagram
#### Python Code
```python
# 26字母数组计数，固定常量空间
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for c in s:
            count[ord(c)-ord('a')] += 1
        for c in t:
            count[ord(c)-ord('a')] -= 1
        for num in count:
            if num != 0:
                return False
        return True
```

```Explanation
Two strings are anagrams only if character frequency matches. Check length first, use a fixed-size array of 26 to count letters, add count for s and subtract for t. All zeros means valid anagram.
```

```Complexity Analysis
Time: O(m+n)
Space: O(1)
```

### 8. Valid Palindrome
#### Python Code
```python
# 双指针向内收缩，跳过符号空格
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
```

```Explanation
Two pointers start from head and tail, skip non-alphanumeric symbols. Convert both characters to lowercase before comparison, return False once mismatch found.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 9. Group Anagrams
#### Python Code
```python
# 排序字符串作为哈希key，分组存储异位词
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)
        return list(groups.values())
```

```Explanation
Anagrams share identical sorted character sequence. Use sorted string as hash key, group all words with matching key together, then return all groups as list.
```

```Complexity Analysis
Time: O(n * k log k)
Space: O(nk)
```

### 10. Longest Substring Without Repeating Characters
#### Python Code
```python
# 滑动窗口+哈希记录字符最新下标
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_pos = {}
        max_len = 0
        left = 0
        for right, c in enumerate(s):
            if c in char_pos and char_pos[c] >= left:
                left = char_pos[c] + 1
            char_pos[c] = right
            max_len = max(max_len, right - left + 1)
        return max_len
```

```Explanation
Sliding window paired with hash map storing last index of each character. If duplicate exists inside window, move left pointer forward to skip duplicate, track maximum window size each iteration.
```

```Complexity Analysis
Time: O(n)
Space: O(min(m,n))
```

### 11. Reverse String
#### Python Code
```python
# 原地双指针交换，禁止额外数组
class Solution:
    def reverseString(self, s: list[str]) -> None:
        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
```

```Explanation
In-place reverse required, two pointers swap left and right characters and move toward center until they meet.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 12. Longest Common Prefix
#### Python Code
```python
# 以第一个字符串为基准逐字符比对
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        base = strs[0]
        for i in range(len(base)):
            c = base[i]
            for word in strs[1:]:
                if i >= len(word) or word[i] != c:
                    return base[:i]
        return base
```

```Explanation
Take first string as base prefix, compare each character with other strings. Mismatch or shorter word means we hit prefix boundary, return sliced base string immediately.
```

```Complexity Analysis
Time: O(m*n)
Space: O(1)
```


