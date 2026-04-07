from collections import defaultdict
t = int(input())
for _ in range(t):
  n, k = map(int, input().split())
  color = input()

  white = 0
  minWhite = float('inf')
  l = 0
  r = 0
  while r < n:
    length = r - l + 1
    # Keep number of white within a window size of k
    if length <= k:
      if color[r] == "W":
        white += 1
    
    # If we reached the window size move left one step and count white again
    if length == k:
      minWhite = min(minWhite, white)
      if color[l] == "W":
        white -= 1
      l += 1

    r += 1
    
  print(minWhite)