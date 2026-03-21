n, m = map(int, input().split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
pairs = 0
 
i = 0
j = 0
while i < n and j < m:
  if array1[i] > array2[j]:
    j += 1
  elif array1[i] < array2[j]:
    i += 1
  else:
    num = array1[i]
    count1, count2 = 0, 0
 
    while i < n and array1[i] == num:
      count1 += 1
      i += 1
    
    while j < m and array2[j] == num:
      count2 += 1
      j += 1
 
    pairs += count1 * count2
 
print(pairs)