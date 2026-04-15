t = int(input())
for _ in range(t):
  n, k = map(int, input().split())
  casinos = []
  for i in range(n):
    _tuple = tuple(map(int, input().split()))
    casinos.append(_tuple)

  casinos.sort(key=lambda x: x[2])

  for l, r, real in casinos:
    if l <= k <= r:
      if real > k:
        k = real

  print(k)