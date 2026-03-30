from collections import Counter
T = int(input())
for _ in range(T):
  s = input()
  t = input()

  s_freq = Counter(s)
  t_freq = Counter(t)
  for char, freq in s_freq.items():
    if char not in t_freq or t_freq[char] < freq:
      print("Impossible")
      break
  else:
    for char, freq in s_freq.items():
      t_freq[char] -= freq

    ans = ""
    i = 0
    for char in sorted(t_freq):
      while i < len(s) and char >= s[i]:
          ans += s[i]
          i += 1
        
      while t_freq[char] != 0:
        ans += char
        t_freq[char] -= 1

    while i < len(s):
      ans += s[i]
      i += 1

    print(ans)