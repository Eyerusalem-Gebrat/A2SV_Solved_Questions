n, k = map(int, input().split())
a = list(map(int, input().split()))
 
count = {} 
left = 0
unique = 0
result = 0
 
for right in range(n):
    if a[right] not in count or count[a[right]] == 0:
        unique += 1
        count[a[right]] = 0
    count[a[right]] += 1
 
    while unique > k:
        count[a[left]] -= 1
        if count[a[left]] == 0:
            unique -= 1
        left += 1
 
    result += (right - left + 1)
 
print(result)