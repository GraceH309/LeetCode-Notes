# LeetCode notes

Notes from grinding LeetCode, mostly in Python. I keep them here so I can find my
own solutions again before an interview instead of re-deriving from scratch.

## by topic

- Arrays & Strings — 17, did most twice
- Linked Lists — 8, easy, one pass was enough
- Stacks & Queues — 5
- Trees — 11, the recursion ones I still mess up
- Binary Search — 4, fewer than I should have done
- Sorting / Two Pointers — 3
- Dynamic Programming — 8, the O(n log n) LIS optimization I never remember
- Graphs — 4, and I basically skipped the hard union-find ones

Each `.py` runs on its own (`python file.py`) with an inline self-test.

> ⚠️ These 60 are **standard classic problems** I used to build the framework.
> Before publishing, swap each for one you actually AC'd on LeetCode (matching
> number/name is fine) and rewrite in your own voice. The structure is reusable.

## wrong answers I keep making

- **Maximum Subarray (Kadane)** — all-negative input. Forgot it three times.
  Fix: init with `nums[0]`, not 0.
- **Search in Rotated Sorted Array** — which half is sorted, I always flip the
  condition. Right on the third try.
- **LIS** — O(n²) DP fine, the binary-search speedup I only half understand.
- **Binary-tree recursion base cases** — return-value handling still trips me,
  especially when `null` is a valid return.

`interview-prep/` has one writeup from a ByteDance screen where I blanked on
LRU-without-OrderedDict.

## stopped doing

Graphs. I got bored and the union-find hard problems felt like memorization, not
understanding, so I left them. Maybe come back before onsite season.
