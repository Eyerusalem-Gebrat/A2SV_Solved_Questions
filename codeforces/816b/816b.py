n, k, q = map(int, input().split())
 
MAX = 200000
diff = [0] * (MAX + 2)
 
for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1
 
freq = [0] * (MAX + 1)
freq[1] = diff[1]
for i in range(2, MAX + 1):
    freq[i] = freq[i - 1] + diff[i]
 
good = [0] * (MAX + 1)
for i in range(1, MAX + 1):
    if freq[i] >= k:
        good[i] = 1
 
prefix = [0] * (MAX + 1)
prefix[1] = good[1]
for i in range(2, MAX + 1):
    prefix[i] = prefix[i - 1] + good[i]
 
for _ in range(q):
    a, b = map(int, input().split())
    print(prefix[b] - prefix[a - 1])