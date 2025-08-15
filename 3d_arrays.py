""" Given an array of 'n' integer numbers, create a 3D array where each sub-array 
        has 3 values:
            1. The value of the original number minus the previous number (if the number is index 0 then use the last in the array).
            2. The original number
            3. The value of the original number plus the next number(if the number is the last index then use the 1st in the array).
"""

import random

def transform(arr):
    arr = random_num()
    n = len(arr)
    
    d_list = [[0, arr[i], 0]  for i in range(n)]
    
    print(d_list)
    
    for i in range(n):
        for j in range(3):
            
            if j == 0 : 
                d_list[i][j] = arr[i] - arr[i-1]
            elif j == 1:
                d_list[i][j] = arr[i]
            elif j == 2: 
                d_list[i][j] = arr[i] + arr[(i+1) % n]
        
    print(d_list)       
                

def random_num():
    n = int(input("Enter the length of the array: "))
    
    for _ in range(n):
        build_arr = random.randint(1, 10)
        arr.append(build_arr)
        
    return arr
    
""" def read_num():
    n = input("Enter the length of the array: ")
    n_int = int(n)
    
    for _ in range(n_int):
        build_arr = input("Enter a number for the array: ")
        build_arr_int = int(build_arr)
        arr.append(build_arr_int)
        print(arr) """

if __name__ == '__main__':
    arr = []
    transform(arr)