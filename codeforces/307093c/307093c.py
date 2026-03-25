n, s = map(int, input().split())
nums = list(map(int, input().split()))
 
curSum = 0
good  = 0
l = 0
for r in range(n):
    curSum += nums[r]
    
    while curSum > s:
        curSum -= nums[l]
        l += 1
    
    good += (r - l + 1)
 
print(good)