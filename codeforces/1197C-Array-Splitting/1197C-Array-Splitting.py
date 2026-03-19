n, k = map(int, input().split())
nums = list(map(int, input().split()))
splits = []
totalCost = max(nums) - min(nums)

for i in range(n-1):
  dif = nums[i+1] - nums[i]
  splits.append(dif)

splits.sort(reverse=True)

i = 0
while k > 1 and i < len(splits):
  totalCost -= splits[i]
  k -= 1
  i += 1

print(totalCost)