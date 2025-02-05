tokens = ["2","1","+","3","*"]
tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
operators = set(['+', '-', '*', '/'])
stack = []
for i in tokens:
    if i not in operators:
        stack.append(i)
    else:
        op2 = stack.pop()
        op1 = stack.pop()
        infix = f"({op1} {i} {op2})"
        stack.append(infix)
rst = stack.pop()
print(eval(rst))