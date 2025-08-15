import random

def merge_sort(arr:list):    
    if (len(arr) <= 1):
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    print(left_half, right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    while (i < len(left) and j < len(right)):
        
        if (left[i] < right[i]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(25)]
    print(arr)
    sorted_arr = merge_sort(arr)
    print(merge_sort)