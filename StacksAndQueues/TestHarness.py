from DataStructures import Collections
from Error import Exceptions

print("\nUnit tests for Stack class\n")

numpassed = 0
numtests = 0

# Test case 1 - create stack
numtests += 1
s = Collections.Stack()
if s.get_count() == 0:
    print("PASSED: Created stack successfully")
    numpassed += 1
else:
    print("FAILED: Could not create stack")

# Test case 2 - push values

numtests += 1
s.push("beep")
s.push("boop")
s.push("skr")
s.push("ding")
s.push(200)
if s.get_count() == 5:
    print("PASSED: pushed five values on successfully")
    numpassed += 1
else:
    print("FAILED: Could not push values")

# Test case 3 - pop empty stack

numtests += 1
try:
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
except Exceptions.ListError as e:
    print(e.message)
    print("PASSED: Exception thrown as expected")
    numpassed += 1
else:
    print("FAILED: Popped value from empty stack")

print("\nUnit tests for Queue class\n")

# Test case 1 - create queue
numtests += 1
q = Collections.Queue()
if q.get_count() == 0:
    print("PASSED: Created queue successfully")
    numpassed += 1
else:
    print("FAILED: Could not create queue")

# Test case 2 - enqueue values

numtests += 1
q.enqueue(100)
q.enqueue(200)
if q.get_count() == 2:
    print("PASSED: enqueued two values on successfully")
    numpassed += 1
else:
    print("FAILED: Could not enqueue values")

# Test case 3 - dequeue empty queue

numtests += 1
try:
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
except Exceptions.ListError as e:
    print(e.message)
    print("PASSED: Exception thrown as expected")
    numpassed += 1
else:
    print("FAILED: Dequeue value from empty queue")

# Results
print("\nPassed ", numpassed, " of ", numtests, " tests: ",
      100*numpassed/numtests, "%\n")