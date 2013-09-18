def binary_search(A, s, t, x):
  if t - s < 0:
    return t + 1
  if s == t:
    if A[s] >= x:
      return t
    else:
      return t + 1
  mid = (s + t) / 2
  y = A[mid]
  if y < x:
    return binary_search(A, mid + 1, t, x)
  if y >= x:
    return binary_search(A, s, mid, x)

array = [0, 1, 2, 4, 6, 7, 7, 10, 11, 15]

print binary_search(array, 0, len(array) - 1, -1)
print binary_search(array, 0, len(array) - 1, 0)
print binary_search(array, 0, len(array) - 1, 1)
print binary_search(array, 0, len(array) - 1, 2)
print binary_search(array, 0, len(array) - 1, 3)
print binary_search(array, 0, len(array) - 1, 4)
print binary_search(array, 0, len(array) - 1, 5)
print binary_search(array, 0, len(array) - 1, 6)
print binary_search(array, 0, len(array) - 1, 7)
print binary_search(array, 0, len(array) - 1, 8)
print binary_search(array, 0, len(array) - 1, 14)
print binary_search(array, 0, len(array) - 1, 15)
print binary_search(array, 0, len(array) - 1, 16)
