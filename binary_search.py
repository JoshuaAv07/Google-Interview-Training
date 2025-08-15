import random

def search(array:list, x: int, left:int, right:int) -> bool:
    if left > right:
        return False
    
    mid = left + ((right - left) // 2)
    
    if (array[mid] == x):
        return True
    elif (x < array[mid]):
        return search(array, x , left, mid-1)
    elif (x > array[mid]):
        return search(array, x , mid+1, right)

if __name__ == "__main__":
    array = sorted([random.randint(1,50) for _ in range(25)])
    print(array)
    res = search(array, 32, 0, len(array)-1)
    print(res)