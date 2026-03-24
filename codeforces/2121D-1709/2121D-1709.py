t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
 
  oprs = 0
  swaps = []
 
  for i in range(n):
    if a[i] > b[i]:
      a[i], b[i] = b[i], a[i]
      oprs += 1
      swaps.append((3, i+1))
 
  for j in range(n):
    for i in range(n-1):
      if a[i] > a[i+1]:
        a[i], a[i+1] = a[i+1], a[i]
        oprs += 1
        swaps.append((1, i+1))
 
  for j in range(n):
    for i in range(n-1):
      if b[i] > b[i+1]:
        b[i], b[i+1] = b[i+1], b[i]
        oprs += 1
        swaps.append((2, i+1))
 
  for i in range(n):
    if a[i] > b[i]:
      a[i], b[i] = b[i], a[i]
      oprs += 1
      swaps.append((3, i+1))
 
  print(oprs)
  for swap in swaps:
    print(*swap)