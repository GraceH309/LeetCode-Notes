# LeetCode Self-Practice Notes
I sorted these classic algorithm problems by category for regular review.
Every single problem contains three parts: clean Python code, short explanation, and time & space complexity analysis.

## Catalog
1. Array & String (12)
2. Linked List (8)
3. Stack & Queue (5)
4. Binary Tree (10)
5. Binary Search & Sort (5)
6. Dynamic Programming (3)

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

# 2. Linked List (8)
### 1. Reverse Linked List
#### Python Code
```python
# 迭代原地反转，空间最优
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
```

```Explanation
Iterative in-place reverse: store next node temporarily, redirect current node to previous node, shift pointers forward. prev becomes new head after loop ends.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 2. Merge Two Sorted Lists
#### Python Code
```python
# 虚拟头节点规避空链表边界判断
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2
        return dummy.next
```

```Explanation
Dummy head avoids empty edge case handling. Pick smaller node from two sorted lists each iteration, link to new chain, attach leftover nodes at last.
```

```Complexity Analysis
Time: O(m+n)
Space: O(1)
```

### 3. Linked List Cycle
#### Python Code
```python
# 快慢指针龟兔赛跑，无额外存储
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

```Explanation
Fast & slow pointer technique: slow moves 1 step, fast moves 2 steps. If cycle exists they will collide; fast hits null if no cycle.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 4. Remove Nth Node From End
#### Python Code
```python
# 快慢指针拉开n步距离，虚拟头处理删头节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        slow = fast = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
```

```Explanation
Dummy head handles edge case of deleting first node. Fast pointer moves n steps ahead, then both move together. Slow lands on predecessor of target node to skip it.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 5. Palindrome Linked List
#### Python Code
```python
# 快慢找中点+反转后半段，原地操作空间O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
```

```Explanation
Find middle node with fast/slow pointer, reverse second half of list, compare values of first half and reversed second half. No extra array storage needed.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 6. Intersection of Two Linked Lists
#### Python Code
```python
# 双指针交换链表遍历，总路程相等必相遇
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
```

```Explanation
Two pointers traverse list A and B, switch to opposite list when reaching end. Total travel distance equal, they meet at intersection node or both hit null.
```

```Complexity Analysis
Time: O(m+n)
Space: O(1)
```

### 7. Remove Duplicates from Sorted List
#### Python Code
```python
# 有序链表单次遍历去重
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
```

```Explanation
Sorted linked list, skip duplicate next node if values match, move forward only when values differ. Single pass solution.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 8. Middle of Linked List
#### Python Code
```python
# 快慢指针一次遍历找中点
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

```Explanation
Fast pointer moves two steps, slow one step. Slow pointer lands on middle node when fast reaches end of list.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

# 3. Stack & Queue (5)
### 1. Valid Parentheses
#### Python Code
```python
# 栈匹配括号，哈希存储对应关系
class Solution:
    def isValid(self, s: str) -> bool:
        match = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c not in match:
                stack.append(c)
            else:
                if not stack or stack.pop() != match[c]:
                    return False
        return len(stack) == 0
```

```Explanation
Push left brackets to stack. When seeing right bracket, pop top element and check match. Empty stack at end means all brackets closed properly.
```

```Complexity Analysis
Time: O(n)
Space: O(n)
```

### 2. Min Stack
#### Python Code
```python
# 双栈结构，O(1)获取最小值
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]
```

```Explanation
Two stacks: main stack stores all values, min stack tracks minimum value at each stage. Pop min stack when popped value equals current min, O(1) get minimum.
```

```Complexity Analysis
Time: O(1)
Space: O(n)
```

### 3. Implement Queue using Stacks
#### Python Code
```python
# 双栈模拟队列，摊还复杂度O(1)
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    def push(self, x: int) -> None:
        self.in_stack.append(x)
    def transfer(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
    def pop(self) -> int:
        self.transfer()
        return self.out_stack.pop()
    def peek(self) -> int:
        self.transfer()
        return self.out_stack[-1]
    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0
```

```Explanation
Two stacks: in stack for push, out stack for pop/peek. Transfer all elements only when out stack empty, amortized O(1) each operation.
```

```Complexity Analysis
Time: Amortized O(1)
Space: O(n)
```

### 4. Daily Temperatures
#### Python Code
```python
# 单调递减栈存储下标，找下一个更大元素
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                res[prev_idx] = idx - prev_idx
            stack.append(idx)
        return res
```

```Explanation
Monotonic decreasing stack stores indexes. When current temp higher than stack top index temp, calculate day difference and fill result array.
```

```Complexity Analysis
Time: O(n)
Space: O(n)
```

### 5. Evaluate Reverse Polish Notation
#### Python Code
```python
# 后缀表达式栈计算，注意除法向零取整
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops = {"+","-","*","/"}
        stack = []
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    stack.append(a+b)
                elif t == "-":
                    stack.append(a-b)
                elif t == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a / b))
        return stack[0]
```

```Explanation
Push numbers to stack. When operator appears, pop two operands and compute. Division truncates toward zero instead of floor division.
```

```Complexity Analysis
Time: O(n)
Space: O(n)
```

# 4. Binary Tree (10)
### 1. Maximum Depth of Binary Tree
#### Python Code
```python
# DFS递归求树深度
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_d = self.maxDepth(root.left)
        right_d = self.maxDepth(root.right)
        return max(left_d, right_d) + 1
```

```Explanation
Recursive DFS: empty node depth 0, current depth = max(left subtree depth, right subtree depth) + 1.
```

```Complexity Analysis
Time: O(n)
Space: O(h)
```

### 2. Invert Binary Tree
#### Python Code
```python
# 递归交换左右子树完成镜像翻转
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```

```Explanation
Recursively invert left and right subtree of every node, swap children after recursion completes.
```

```Complexity Analysis
Time: O(n)
Space: O(h)
```

### 3. Same Tree
#### Python Code
```python
# 递归逐层比对节点
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

```Explanation
Base case: both null → True; one null → False; value mismatch → False. Recursively check left and right child pairs.
```

```Complexity Analysis
Time: O(n)
Space: O(h)
```

### 4. Subtree of Another Tree
#### Python Code
```python
# 嵌套辅助函数判断两棵树完全相等
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def same(a,b):
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            return same(a.left,b.left) and same(a.right,b.right)
        if not root:
            return False
        if same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
```

```Explanation
Helper function checks identical trees. Traverse every node in main tree, return True if any node matches subtree root fully.
```

```Complexity Analysis
Time: O(m*n)
Space: O(h)
```

###5. Lowest Common Ancestor
#### Python Code
```python
# 后序递归查找最近公共祖先
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
```

```Explanation
Return node if hit p/q. If left and right both return non-null, current node is LCA. Pass non-null result upward otherwise.
```

```Complexity Analysis
Time: O(n)
Space: O(h)
```

###6. Binary Tree Level Order Traversal
#### Python Code
```python
# BFS队列层序遍历
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            level = []
            sz = len(q)
            for _ in range(sz):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
```

```Explanation
BFS with queue, record size of queue before each layer to separate levels, collect values per layer into 2D list.
```

```Complexity Analysis
Time: O(n)
Space: O(h)
```

###7. Validate BST
#### Python Code
```python
# DFS携带上下边界校验二叉搜索树
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        return dfs(root, float('-inf'), float('inf'))
```

```Explanation
Recursive DFS with value bounds. Left subtree values < current val, right subtree > current val, update bounds for child nodes recursively.
```

```Complexity Analysis
Time: O(n)
Space: O(h)
```

###8. Kth Smallest Element in BST
#### Python Code
```python
# BST中序遍历升序，迭代计数到第k个节点返回
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        cur = root
        cnt = 0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cnt += 1
            if cnt == k:
                return cur.val
            cur = cur.right
        return -1
```

```Explanation
In-order traversal of BST yields sorted values. Count visited nodes, return value when count reaches k without full tree traversal.
```

```Complexity Analysis
Time: O(h+k)
Space: O(h)
```

###9. Path Sum
#### Python Code
```python
# 递归递减目标值，叶子节点判断匹配
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        sub = targetSum - root.val
        return self.hasPathSum(root.left, sub) or self.hasPathSum(root.right, sub)
```

```Explanation
Subtract current node value from target each recursion. Check if leaf value equals remaining target when reaching leaf node.
```

```Complexity Analysis
Time: O(n)
Space: O(h)
```

###10. Binary Tree Diameter
#### Python Code
```python
# 后序求深度同步更新全局最大直径
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_d = 0
        def depth(node):
            if not node:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            self.max_d = max(self.max_d, l + r)
            return max(l, r) + 1
        depth(root)
        return self.max_d
```

```Explanation
Calculate subtree depth recursively, update global max diameter with sum of left & right depth at each node.
```

```Complexity Analysis
Time: O(n)
Space: O(h)
```

# 5. Binary Search & Sort (5)
### 1. Binary Search
#### Python Code
```python
# 标准左闭右闭区间二分查找
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
```

```Explanation
Classic binary search with closed interval [l, r]. Adjust left/right bound based on mid value, return index if target found.
```

```Complexity Analysis
Time: O(log n)
Space: O(1)
```

### 2. Search Insert Position
#### Python Code
```python
# 二分查找，循环结束l即为插入位置
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
```

```Explanation
Binary search, variable l stores insert index after loop ends, works for all edge cases of target size.
```

```Complexity Analysis
Time: O(log n)
Space: O(1)
```

### 3. First Bad Version
#### Python Code
```python
# API接口已定义，二分查找左边界
def isBadVersion(version: int) -> bool:
    pass
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l
```

```Explanation
Binary search left boundary of bad version. Narrow right bound if mid is bad, move left forward if mid good. l == r at exit.
```

```Complexity Analysis
Time: O(log n)
Space: O(1)
```

### 4. Find Peak Element
#### Python Code
```python
# 二分找峰值，峰值一定存在
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l
```

```Explanation
Peak always exists. If mid > mid+1, peak lies left half; else right half, shrink range until l == r.
```

```Complexity Analysis
Time: O(log n)
Space: O(1)
```

### 5. Search in Rotated Sorted Array
#### Python Code
```python
# 旋转有序数组二分，先判断有序区间
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
```

```Explanation
Rotated sorted array binary search. Check which half is sorted, judge if target inside sorted range to adjust bounds.
```

```Complexity Analysis
Time: O(log n)
Space: O(1)
```

# 6. Dynamic Programming (3)
### 1. Climbing Stairs
#### Python Code
```python
# dp滚动变量优化空间，类斐波那契
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n+1):
            c = a + b
            a = b
            b = c
        return b
```

```Explanation
DP recurrence: dp[i] = dp[i-1] + dp[i-2]. Optimize space with two rolling variables instead of full array.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 2. House Robber
#### Python Code
```python
# 滚动变量压缩dp空间，不能抢相邻房屋
class Solution:
    def rob(self, nums: list[int]) -> int:
        prev1, prev2 = 0, 0
        for num in nums:
            cur = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = cur
        return prev1
```

```Explanation
Cannot rob adjacent houses. Current max = max(skip current, rob current + two houses before). Rolling variables save space.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 3. House Robber II
#### Python Code
```python
# 环形房屋拆分成两种线性情况分别计算
class Solution:
    def rob(self, nums: list[int]) -> int:
        def sub_rob(arr):
            p1, p2 = 0, 0
            for n in arr:
                c = max(p1, p2 + n)
                p2 = p1
                p1 = c
            return p1
        if len(nums) == 1:
            return nums[0]
        return max(sub_rob(nums[1:]), sub_rob(nums[:-1]))
```

```Explanation
Houses form circle, first and last cannot be robbed together. Compute max of two subarrays: exclude first, exclude last.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

