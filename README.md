# LeetCode grind log

> Organized by category for easy review. Some problems I had to do three times before they stuck.

> ⚠️ Note: these 60 problems are **standard classic problems** I used to practice
> and to build this notes framework. Before you publish, swap each one for a
> problem **you actually AC'd on LeetCode** (matching the number/name is fine),
> and rewrite the solutions in your own voice — don't copy. The framework and
> structure are free to reuse.

## Progress tracker

| Category | Folder | 1st pass | 2nd | 3rd |
|----------|--------|----------|-----|-----|
| Array & String | `Arrays_Strings/` | 17 | 12 | 4 |
| Linked List | `Linked_Lists/` | 8 | 5 | 2 |
| Stack & Queue | `Stacks_Queues/` | 5 | 3 | 1 |
| Tree | `Trees/` | 11 | 6 | 2 |
| Binary Search | `Binary_Search/` | 4 | 3 | 2 |
| Sort & Two Pointers | `Sorting_Two_Pointers/` | 3 | 2 | 1 |
| DP | `Dynamic_Programming/` | 8 | 4 | 1 |
| Graph | `Graphs/` | 4 | 2 | 0 |

Each `.py` runs on its own (`python xxx.py`) with an `if __name__ == "__main__"` self-test.

## Wrong-answer notebook (stuff I keep getting wrong)

1. **53. Maximum Subarray (Kadane)**
   - Why wrong: with all-negative input you can't default to 0. My first version did `cur = 0` init and failed.
   - 3rd time making this mistake — must remember `cur = max(num, cur + num)` with init from the first element.

2. **33. Search in Rotated Sorted Array**
   - Why wrong: always reversed the "which half is sorted" logic. Failed again on the 2nd pass, got it on the 3rd with a drawing.

3. **300. LIS (Longest Increasing Subsequence)**
   - Why wrong: O(n²) DP I can write; the O(n log n) binary-search optimization I never remember.
   - If it shows up in an interview, write O(n²) first to be safe.

4. **Binary-tree recursion base cases**
   - Return-value handling still trips me up, especially when `null` is a valid return.

## Grind log (excerpt)

| Problem | Date | Status | Note |
|---------|------|--------|------|
| 1. Two Sum | 7/1 | ✅ | first version brute force O(n²), got TLE |
| 1. Two Sum | 7/2 | ✅ | read solution, hash map, O(n), remembered it |
| 53. Maximum Subarray | 7/3 | ❌ | all-negative case wrong, forgot init |
| 53. Maximum Subarray | 7/10 | ✅ | fixed only on 2nd pass |
| 33. Search in Rotated | 7/12 | ❌ | rotated-array boundary reversed again |
| 33. Search in Rotated | 7/25 | ✅ | 3rd pass, figured it out with a picture |

## First-version-wrong → fixed (example)

Using **53. Maximum Subarray** as an example — I try to keep this "trip-up" trail in each file too:

**First version (wrong):**
```python
cur = 0          # wrong! returns 0 on all-negative
best = 0
for x in nums:
    cur = max(x, cur + x)
    best = max(best, cur)
# test [-2,-1] returns 0, expected -1. Failed.
```

**Second version (right):**
```python
cur = best = nums[0]   # init from first element
for x in nums[1:]:
    cur = max(x, cur + x)
    best = max(best, cur)
```

## interview-prep/

`interview-prep/` holds the problem lists and retrospectives before each interview; there's one ByteDance sample in there now.
