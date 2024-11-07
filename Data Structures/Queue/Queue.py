#queues implemented as deque in python
import collections

queue = collections.deque()

queue.append(1)
queue.append(2)
queue.append(3)

print("the queue", list(queue))

front_element = queue.popleft()
print("front element removed: ", front_element)

if queue:
    front_element = queue[0]
    print("front element not removed", front_element)

