t = int(input())
for _ in range(t):
  n = int(input())
  red = list(map(int, input().split()))
  m = int(input())
  blue = list(map(int, input().split()))
 
  for i in range(1, n):
    red[i] = red[i-1] + red[i]
 
  for i in range(1, m):
    blue[i] = blue[i-1] + blue[i]
 
  max1 = max(0, max(red))
  max2 = max(0, max(blue))
 
  print(max1 + max2)