from collections import Counter

def find_odd_flavour(N, C):
    flavour_count = Counter(C)
    
    for flavour in C:
        if flavour_count[flavour] % 2 != 0:
            return flavour
    
    return "All are even"

N = int(input())

C = []
for _ in range(N):
    flavour = input().strip()
    C.append(flavour)

result = find_odd_flavour(N, C)

print(result)
