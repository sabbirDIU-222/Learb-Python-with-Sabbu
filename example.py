'''

stack and queue
we use it often but don't understand it
stact is a things that we know last in first out
that means who come in last he served first
push pop

in queue we use first in first out
that means who come first he will served first
'''

 # taking a  list

corroption = ["jaforullah","rodro","a ho mo nasim"]
corroption.pop()
print(corroption)
corroption.pop()
corroption.pop()
if not corroption:
    print("all item cleared")
# in pop

from collections import deque

student = deque(["a","b","c"])
student.popleft()
print(student)





