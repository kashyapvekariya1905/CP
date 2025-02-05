s = "(1+(4+5+2)-3)+(6+8)"
# 23
stack = []
sum = 0
sign = 1
op = 0
for i in s :
    if i.isdigit():
        op = op*10 + int(i)
    elif i == '+':
        sum+=sign*op
        op = 0
        sign = 1
    elif i == '-':
        sum += sign*op
        sign = -1
        op = 0
    elif i == '(':
        stack.append(sum)
        stack.append(sign)
        sum = 0
        sign = 1
    elif i == ')':
        sum += sign*op
        op = 0
        sum *= stack.pop()
        sum += stack.pop()
sum += sign *op
print(sum)