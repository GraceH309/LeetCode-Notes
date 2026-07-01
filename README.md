# LeetCode Self-Practice Notes
I sorted these classic algorithm problems by category for regular review.
Every single problem contains three parts: clean Python code, short explanation, and time & space complexity analysis.

## Catalog
1. Array & String (2)
2. Linked List ()
3. Stack & Queue ()
4. Binary Tree ()
5. Binary Search & Sort ()
6. Dynamic Programming ()

---

# 1. Array & String (2)
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

