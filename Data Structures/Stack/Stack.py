#stacks are implemented as lists in python
stack = []

#add an item to the stack
stack.append(1)
stack.append(2)
stack.append(3)


#pop the most recently added item from the stack
top_element = stack.pop()
print("top of stack (removed): ", top_element)


#peek at the top element without removing if
if stack:
    top_element = stack[-1]
    print("top of stack (not removed): ", top_element)