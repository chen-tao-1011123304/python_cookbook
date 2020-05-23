from collections import deque


q = deque()

q.append(1)
q.append(2)
q.append(3)

print(q)  # 123

q.appendleft(4)
print(q)  # 4123

a = q.pop()
print(a)  # 3

b = q.popleft()
print(b)  # 4





