#pop/top/push/empty
stack = []
for c in range(0, 10):
    stack.append(c)
    print(stack, f'top = {len(stack)-1}')

stack.pop()
#empty indica a pilha vazia
