n, s = map(int, input().split())
nums = list(map(int, input().split()))
 
curSum = 0
good = 0
l = 0
r = 0
while r < n:
  curSum += nums[r]
  
  while curSum >= s:
    good += n - r
    curSum -= nums[l]
    l += 1
 
  r += 1
 
print(good)