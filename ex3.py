from collections import deque

def min_of_maximums(arr, k):
    n = len(arr)
    dq = deque()
    min_of_max = float('inf')
    
    for i in range(n):
        if dq and dq[0] <= i - k:
            dq.popleft()
        
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            max_in_window = arr[dq[0]]
            min_of_max = min(min_of_max, max_in_window)
    
    return min_of_max

k = int(input())
n = int(input())
arr = [int(input()) for _ in range(n)]

result = min_of_maximums(arr, k)
print(result)
