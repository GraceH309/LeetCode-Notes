"""
Implement Queue using Stacks  (Easy)
LeetCode #232  -  Topic: Stacks & Queues

Approach: see function docstring / inline comments.
"""
class MyQueue:
    def __init__(self):
        self.inp = []; self.out = []
    def push(self, x):
        self.inp.append(x)
    def pop(self):
        self._drain(); return self.out.pop()
    def peek(self):
        self._drain(); return self.out[-1]
    def empty(self):
        return not self.inp and not self.out
    def _drain(self):
        if not self.out:
            while self.inp: self.out.append(self.inp.pop())

if __name__ == "__main__":
    q = MyQueue(); q.push(1); q.push(2); assert q.peek() == 1; assert q.pop() == 1; assert q.empty() is False
    print("OK - my_queue")
