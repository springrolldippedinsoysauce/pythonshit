from Heaps import Heap
import random

data = ['Pomeranian', "Siberian Husky", "German Shepherd", "Golden Retriever", "Labrador Retriever"]
ret = ['Pomeranian', 'German Shepherd', 'Labrador Retriever', 'Siberian Husky', 'Golden Retriever']
priority = [5, 2, 4, 1, 3]
passed = True

heap = Heap.Heap(len(data))

print("=================Testing add():=================")
print("Adding Priority: ", priority)
print("Adding Value: ", data)
for i in range(len(data)):
    heap.add(priority[i], data[i])

print("=================Testing remove():=================")
for i in range(len(data)):
    get = heap.remove()
    passed = passed and get == ret[i]
    print(get)
print("Heap add() and remove() test status: ", "passed" if passed is True else "failed")

test = []
for i in range(1000):
    key = int(random.random() * 1000)
    test.append(Heap.HeapEntry(key, 0))

heap.heap_sort(test)

for i in range(len(test)):
    passed = passed and test[i].get_priority() <= test[i+1].get_priority()
print("\nHeapSort status:", "passed" if passed is True else "failed")