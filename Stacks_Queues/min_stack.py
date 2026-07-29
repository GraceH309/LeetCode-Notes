"""
Min Stack  (Medium)
LeetCode #155  -  Topic: Stacks & Queues

Approach: see function docstring / inline comments.
"""
class MinStack:
    def __init__(self):
        self.s = []
    def push(self, x):
        m = x if not self.s else min(x, self.s[-1][1])
        self.s.append((x, m))
    def pop(self):
        return self.s.pop()[0]
    def top(self):
        return self.s[-1][0]
    def get_min(self):
        return self.s[-1][1]

if __name__ == "__main__":
    ms = MinStack(); ms.push(-2); ms.push(0); ms.push(-3)
    assert ms.get_min() == -3; ms.pop(); assert ms.top() == 0; assert ms.get_min() == -2
    print("OK - min_stack")
