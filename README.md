# LeetCode Self-Practice Notes
I categorize these classic algorithm problems for regular review.
For each problem, I organize three parts: clean Python implementation, personal understanding, and complexity analysis.

## Catalog
1. Array & String (12)
2. Linked List (8)
3. Stack & Queue (5)
4. Binary Tree (10)
5. Binary Search & Sort (5)
6. Dynamic Programming (10)

---

# 1. Array & String (12)
### 1. Two Sum
#### Python Code
```python
# Pitfall: brute force double loops will get TLE on large test cases. Hash table one-pass is the standard optimal way.
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
I wrote the nested loop first during practice, obviously too slow for big data. The core idea is storing value-index mapping in dict while iterating, check if needed complement exists. Return immediately once found.
```

```Complexity Analysis
Time: O (n)
Space: O (n)
```

### 2. Best Time to Buy & Sell Stock
#### Python Code
```python
# At first I tried two-way traversal, totally unnecessary. Just track the minimum price we’ve met so far.
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
Only buy before sell. Keep updating the lowest buying point, calculate profit every time price rises above it. Single pass enough.
```

```Complexity Analysis
Time: O(n)
Space: O(1), only two variables used
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
Super straightforward. Use set to record appeared numbers, early return once duplicate hit.
```

```Complexity Analysis
Time: O(n)
Space: O(n)
```

### 4. Product of Array Except Self
#### Python Code
```python
# Cannot use division per problem rule. Calculate left prefix product and right suffix product separately.
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]
        right = 1
        for i in range(n-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
```

```Explanation
Result for position i = product of all left numbers × product of all right numbers. Two traversals finish the job, avoid division edge case with zero.
```

```Complexity Analysis
Time: O(n)
Space: O(n)
```

### 5. Maximum Subarray
#### Python Code
```python
# Kadane greedy algorithm, need to handle all-negative test case carefully
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
        return max_sum
```

```Explanation
If adding current number makes the current sum worse than the number itself, reset the subarray start here. Don’t forget all-negative input, can’t just return 0.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 6. Maximum Sum Subarray
#### Python Code
```python
# Same problem as No.5 (LC 53), repeat practice to strengthen Kadane logic
# Key takeaway: never default result to 0 when all elements are negative
```

```Explanation
Rewrote this one again to drill the boundary condition. Easy to make a careless mistake here.
.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 7. Valid Anagram
#### Python Code
```python
# Count 26 lowercase letters with fixed array, constant space
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
Length check first as quick filter. Increment count for s, decrement for t. All zeros means frequency fully matched.
```

```Complexity Analysis
Time: O(m+n)
Space: O(1)
```

### 8. Valid Palindrome
#### Python Code
```python
# Two pointers shrink inward, skip non-alphanumeric chars and spaces
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
Lowercase conversion is necessary. Skip symbols before comparison, early return on mismatch.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 9. Group Anagrams
#### Python Code
```python
# Sort each word as hash key to group anagrams together
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
Anagrams have identical sorted string, that’s the core trick here. Simple but effective.
```

```Complexity Analysis
Time: O(n * k log k)
Space: O(nk)
```

### 10. Longest Substring Without Repeating Characters
#### Python Code
```python
# Sliding window + hash map record last occurrence index of each char
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
When duplicate appears inside current window, move left boundary forward to exclude old duplicate. Keep updating window size.
```

```Complexity Analysis
Time: O(n)
Space: O(min(m,n))
```

### 11. Reverse String
#### Python Code
```python
# In-place swap with two pointers, no extra array allowed
class Solution:
    def reverseString(self, s: list[str]) -> None:
        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
```

```Explanation
Straightforward swap from both ends toward center. Problem requires modify input list directly.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 12. Longest Common Prefix
#### Python Code
```python
# Use first string as benchmark, compare char by char with others
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
Once meet shorter string or different character, return the prefix we got so far.
```

```Complexity Analysis
Time: O(m*n)
Space: O(1)
```

# 2. Linked List (8)
### 1. Reverse Linked List
#### Python Code
```python
# Iterative in-place reverse, best space efficiency
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
Temporarily save next node before redirect pointer. Finally prev becomes new head. Recursive version also works but iteration is more intuitive for me.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 2. Merge Two Sorted Lists
#### Python Code
```python
# Dummy head avoids lots of empty list boundary judgment
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
Dummy node is a must-have trick for linked list problems, simplify edge cases a lot. Append remaining nodes at last.
```

```Complexity Analysis
Time: O(m+n)
Space: O(1)
```

### 3. Linked List Cycle
#### Python Code
```python
# Fast & slow pointer (tortoise and hare), no extra memory
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
Classic Floyd cycle detection algorithm. If loop exists fast will catch slow eventually.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 4. Remove Nth Node From End
#### Python Code
```python
# Fast pointer go n steps first, dummy head handle deleting head node case
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
Separate two pointers by n nodes, slow stops at predecessor of target node for deletion.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 5. Palindrome Linked List
#### Python Code
```python
# Find middle point + reverse second half, O(1) space solution
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
Don’t want to store all values in array for space saving. Reverse latter half then compare one by one.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 6. Intersection of Two Linked Lists
#### Python Code
```python
# Two pointers switch list to traverse, same total distance will meet
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
```

```Explanation
Tricky but elegant method. If no intersection both end at None.
```

```Complexity Analysis
Time: O(m+n)
Space: O(1)
```

### 7. Remove Duplicates from Sorted List
#### Python Code
```python
# Single pass deduplication for sorted linked list
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
Sorted list means duplicates are adjacent, skip duplicate directly.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 8. Middle of Linked List
#### Python Code
```python
# One pass find middle node with fast slow pointer
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

```Explanation
Fast moves two steps each time, slow one step. Simple and efficient.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

# 3. Stack & Queue (5)
### 1. Valid Parentheses
#### Python Code
```python
# Use stack for bracket matching, hash table store mapping relation
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
Push left brackets, pop and check match when meet right ones. Empty stack at last means valid.
```

```Complexity Analysis
Time: O(n)
Space: O(n)
```

### 2. Min Stack
#### Python Code
```python
# Double stack design, getMin() O(1) time
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
Auxiliary stack record minimum value at each push operation, pop synchronously.
```

```Complexity Analysis
Time: O(1) for all operations
Space: O(n)
```

### 3. Implement Queue using Stacks
#### Python Code
```python
# Two stacks simulate queue, amortized O(1) each operation
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
Only transfer elements when out_stack is empty, amortized constant time cost).
```

```Complexity Analysis
Time: Amortized O(1)
Space: O(n)
```

### 4. Daily Temperatures
#### Python Code
```python
# Monotonic decreasing stack store index, find next greater element
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
Monotonic stack classic problem. Calculate waiting days when warmer day appears.
```

```Complexity Analysis
Time: O(n)
Space: O(n)
```

### 5. Evaluate Reverse Polish Notation
#### Python Code
```python
# Postfix expression calculate by stack, note division truncate to zero
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
Pay special attention to division in Python, need int() to truncate toward zero instead of floor division.
```

```Complexity Analysis
Time: O(n)
Space: O(n)
```

# 4. Binary Tree (10)
### 1. Maximum Depth of Binary Tree
#### Python Code
```python
# DFS recursive calculate tree depth
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_d = self.maxDepth(root.left)
        right_d = self.maxDepth(root.right)
        return max(left_d, right_d) + 1
```

```Explanation
Post-order traversal, depth = max(left depth, right depth) + 1. Recursion stack take O(h) space.
```

```Complexity Analysis
Time: O(n)
Space: O(h), h is tree height (recursion stack)
```

### 2. Invert Binary Tree
#### Python Code
```python
# Recursively swap left and right subtree for mirror flip
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```

```Explanation
Very concise recursive writing, swap after children inverted.
```

```Complexity Analysis
Time: O(n)
Space: O(h)
```

### 3. Same Tree
#### Python Code
```python
# Recursively compare node structure and value
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
Judge null case first, then value equality, then recurse children.
```

```Complexity Analysis
Time: O(n)
Space: O(h)
```

### 4. Subtree of Another Tree
#### Python Code
```python
# Nested helper function check exact tree match
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
Traverse every node in main tree as possible subtree root, use helper to verify full match.
```

```Complexity Analysis
Time: O(m*n)
Space: O(h)
```

###5. Lowest Common Ancestor
#### Python Code
```python
# Post-order recursion find LCA
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
Core logic: if left and right both return non-null, current node is LCA.
```

```Complexity Analysis
Time: O(n)
Space: O(h)
```

###6. Binary Tree Level Order Traversal
#### Python Code
```python
# BFS queue implement level traversal
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
Record queue size before each layer loop to separate different levels, standard BFS template.
```

```Complexity Analysis
Time: O(n)
Space: O(h)
```

###7. Validate BST
#### Python Code
```python
# DFS with upper & lower bound to verify BST property
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
Left subtree strictly smaller, right strictly larger. Pass updated bound into recursion. Don’t forget strict less than.
```

```Complexity Analysis
Time: O(n)
Space: O(h)
```

###8. Kth Smallest Element in BST
#### Python Code
```python
# BST in-order traversal is ascending order, count until k-th node
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
In-order traversal yields sorted values. Count until k-th element.
```

```Complexity Analysis
Time: O(h+k)
Space: O(h)
```

###9. Path Sum
#### Python Code
```python
# Recursively reduce target value, check leaf node match
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
Only valid path ends at leaf node, important boundary condition.
```

```Complexity Analysis
Time: O(n)
Space: O(h)
```

###10. Binary Tree Diameter
#### Python Code
```python
# Post-order calculate depth, update global max diameter
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
Diameter passing through current node = left depth + right depth. Update global maximum during depth calculation.
```

```Complexity Analysis
Time: O(n)
Space: O(h)
```

# 5. Binary Search & Sort (5)
### 1. Binary Search
#### Python Code
```python
# Standard closed interval [l, r] binary search
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
Basic binary search template, remember loop condition l <= r for closed interval.
```

```Complexity Analysis
Time: O(log n)
Space: O(1)
```

### 2. Search Insert Position
#### Python Code
```python
# Binary search, final l is insert index
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
If target not found, left pointer stops exactly at the insertion position.
```

```Complexity Analysis
Time: O(log n)
Space: O(1)
```

### 3. First Bad Version
#### Python Code
```python
# Binary search left boundary
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
Left boundary binary search template, shrink right when mid is bad.
```

```Complexity Analysis
Time: O(log n)
Space: O(1)
```

### 4. Find Peak Element
#### Python Code
```python
# Binary search find peak, problem guarantee peak exists
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
Move to higher slope side each time, finally converge to peak index.
```

```Complexity Analysis
Time: O(log n)
Space: O(1)
```

### 5. Search in Rotated Sorted Array
#### Python Code
```python
# Binary search on rotated sorted array, judge sorted half first
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
One side of mid must be sorted, check whether target lies inside sorted interval to narrow range.
```

```Complexity Analysis
Time: O(log n)
Space: O(1)
```

# 6. Dynamic Programming (10)
### 1. Climbing Stairs
#### Python Code
```python
# Rolling variable optimize space, Fibonacci-like recurrence
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n+1):
            a, b = b, a + b
        return b
```

```Explanation
dp[i] = dp[i-1] + dp[i-2]. No need full array, only keep last two status.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 2. House Robber
#### Python Code
```python
# Rolling DP variables, cannot rob adjacent houses
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
Two choices each step: rob current or skip it. Keep track of two previous maximum values.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 3. House Robber II
#### Python Code
```python
# Circular array split into two linear subproblems
class Solution:
    def rob(self, nums: list[int]) -> int:
        def sub_rob(arr):
            p1, p2 = 0, 0
            for n in arr:
                c = max(p1, p2 + n)
                p2, p1 = p1, c
            return p1
        if len(nums) == 1:
            return nums[0]
        return max(sub_rob(nums[1:]), sub_rob(nums[:-1]))
```

```Explanation
Circle means first and last can’t both be robbed. Compute max of two cases: remove first / remove last element.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 4. Coin Change
#### Python Code
```python
# Unbounded knapsack DP, init infinity for impossible amount
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for val in range(1, amount+1):
            for c in coins:
                if c <= val:
                    dp[val] = min(dp[val], dp[val - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
```

```Explanation
Classic complete backpack problem. Return -1 if amount can’t be composed by given coins.
```

```Complexity Analysis
Time: O(amount * k)
Space: O(amount)
```

### 5. Unique Paths
#### Python Code
```python
# 2D DP, only move right or down
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
```

```Explanation
First row and column all equal to 1. Path count comes from top cell + left cell.
```

```Complexity Analysis
Time: O(m*n)
Space: O(m*n)
```

### 6. Jump Game
#### Python Code
```python
# Greedy DP, track farthest reachable index
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        far = 0
        for idx, step in enumerate(nums):
            if idx > far:
                return False
            far = max(far, idx + step)
        return True
```

```Explanation
Super concise greedy approach. If current index beyond farthest reachable point, jump impossible.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

### 7. Longest Increasing Subsequence
#### Python Code
```python
# Basic O(n²) DP, dp[i] = LIS length ending at index i
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
```

```Explanation
Double loop brute force DP version, easy to understand. There’s O(n log n) optimization but this one for review base logic.
```

```Complexity Analysis
Time: O(n²)
Space: O(n)
```

###8. Word Break
#### Python Code
```python
# String split DP, dp[i] means first i characters can be segmented
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]
```

```Explanation
Split point j: if s[0:j] valid and s[j:i] in dict, then s[0:i] valid.
```

```Complexity Analysis
Time: O(n²)
Space: O(n)
```

###9. Decode Ways
#### Python Code
```python
# Rolling DP count valid digit decoding methods
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        a, b = 1, 1
        for i in range(1, len(s)):
            cur = 0
            if s[i] != '0':
                cur += b
            two = int(s[i-1:i+1])
            if 10 <= two <= 26:
                cur += a
            a, b = b, cur
        return b
```

```Explanation
Two cases: decode single digit alone, or combine two digits within 10~26. Leading zero directly invalid.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```

###10. Fibonacci Number
#### Python Code
```python
# Iterative Fibonacci with rolling variable optimization
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        x, y = 0, 1
        for _ in range(2, n+1):
            x, y = y, x + y
        return y
```

```Explanation
Pure iterative implementation, avoid recursion stack overhead. Very basic DP entry problem.
```

```Complexity Analysis
Time: O(n)
Space: O(1)
```
