"""
Evaluate Reverse Polish Notation  (Medium)
LeetCode #150  -  Topic: Stacks & Queues

Approach: see function docstring / inline comments.
"""
def eval_rpn(tokens):
    st = []
    for t in tokens:
        if t in "+-*/":
            b, a = st.pop(), st.pop()
            if t == "+": st.append(a+b)
            elif t == "-": st.append(a-b)
            elif t == "*": st.append(a*b)
            else: st.append(int(a/b))
        else:
            st.append(int(t))
    return st[0]

if __name__ == "__main__":
    assert eval_rpn(["2","1","+","3","*"]) == 9
    assert eval_rpn(["4","13","5","/","+"]) == 6
    print("OK - eval_rpn")
