from heap import MinHeap

heap = MinHeap()
heap.insert(10)
heap.insert(5)
heap.insert(20)
heap.insert(2)

print("Heap:", heap)
print("Min element:", heap.peek())
print("Extract min:", heap.extract_min())
print("Heap after extraction:", heap)