import sys

input = sys.stdin.readline
left_stack = list(input().rstrip())
right_stack = []

m = int(input().rstrip())
for _ in range(m):
    command = input().rstrip().split()
    
    if command[0] == 'L' and left_stack:
        right_stack.append(left_stack.pop())
        
    elif command[0] == 'D' and right_stack:
        left_stack.append(right_stack.pop())

    elif command[0] == 'B' and left_stack:
        left_stack.pop()
        
    elif command[0] == 'P':
        left_stack.append(command[1])

sys.stdout.write(''.join(left_stack + right_stack[::-1]))