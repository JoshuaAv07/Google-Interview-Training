from stack import Stack

my_stack = Stack()

print(f'Stack top = {my_stack.top()}')
print(f'Stack size = {my_stack.size()}')
print(f'If stack is empty = {my_stack.empty()}\n')

n = int(input("How many countries you are going to enter: "))
for i in range(1,n+1):
    my_stack.push(input(f"{i}: "))

print(f'Stack top = {my_stack.top()}')
print(f'Stack size = {my_stack.size()}')
print(f'If stack is empty = {my_stack.empty()}\n')

print('\nStack elements\n')

for student in my_stack.iter():
    print(student)

print('\nPop an element\n')
print(my_stack.pop())

print('\nStack elements\n')

for student in my_stack.iter():
    print(student)