# LeetCode Self-Practice Notes
I sorted these classic algorithm problems by category for regular review.
Every single problem contains three parts: clean Python code, short explanation, and time & space complexity analysis.

## Catalog
1. Array & String (6)
2. Linked List ()
3. Stack & Queue ()
4. Binary Tree ()
5. Binary Search & Sort ()
6. Dynamic Programming ()

---

# 1. Array & String (6)
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

