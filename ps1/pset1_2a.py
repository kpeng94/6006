'''
  if s > t: return t + 1

  binary search:
  1. look at middle element: (s + t) / 2  = u
  2. if u > x, we look on the left side(do we do a O(1) check to see if )
  3. if u = x, we store this and look on the left side
  4. If u < x, we look on the right side(no check)
'''
def binary_search(array, s, t, x):
  while s <= t:
    mid = (s + t) / 2
    # Check middle element
    if array[mid] < x:
      # If middle is less than x, we check the right half
      s = mid + 1
    else:
      # If middle is greater than x, we check the left half
      # including this element because it is bigger than x
      t = mid
    # If our next check is an 1 element array
    if s == t:
      if array[t] >= x:
        return t
      else:
        return t + 1
  return t + 1

  # At each step, it either breaks it down into mid -> t or s -> mid
  # a mid b -> b if first case, if b >= x, b is guaranteed to be smallest element bigger than x.
  # if 2nd case, -> a mid, if a < x, a is guaranteed to be largest integer smaller than x
  # mid b -> b if first case. if b >= x b is guaranteed to be smallest > x
  # if 2nd case, -> mid -> always breaks down into 1 element -> mid > x
  # 1 element array. need to show that getting to this point means that
  # this is the smallest element that can be bigger than it and the element to the right
  # is automatically larger than it

def binary_search_min(A, s, t, x):
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
    return binary_search_min(A, mid + 1, t, x)
  if y >= x:
    return binary_search_min(A, s, mid, x)

# array = [0, 1, 1, 2, 3, 3, 3, 3, 4, 5, 5, 6, 6, 6, 6]
array = [0, 1, 2, 4, 6, 7, 7, 10, 11, 15]
# print binary_search_min(array, 0, len(array) - 1, -1)
# print binary_search_min(array, 0, len(array) - 1, 0)
# print binary_search_min(array, 0, len(array) - 1, 1)
# print binary_search_min(array, 0, len(array) - 1, 2)
# print binary_search_min(array, 0, len(array) - 1, 3)
# print binary_search_min(array, 0, len(array) - 1, 4)
# print binary_search_min(array, 0, len(array) - 1, 5)
# print binary_search_min(array, 0, len(array) - 1, 6)
# print binary_search_min(array, 0, len(array) - 1, 7)
# print binary_search_min(array, 0, len(array) - 1, 8)
# print binary_search_min(array, 0, len(array) - 1, 14)
# print binary_search_min(array, 0, len(array) - 1, 15)
# print binary_search_min(array, 0, len(array) - 1, 16)
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


print binary_search_min(array, 0, len(array) - 1, -1)
print binary_search_min(array, 0, len(array) - 1, 0)
print binary_search_min(array, 0, len(array) - 1, 1)
print binary_search_min(array, 0, len(array) - 1, 2)
print binary_search_min(array, 0, len(array) - 1, 3)
print binary_search_min(array, 0, len(array) - 1, 4)
print binary_search_min(array, 0, len(array) - 1, 5)
print binary_search_min(array, 0, len(array) - 1, 6)
print binary_search_min(array, 0, len(array) - 1, 7)
print binary_search_min(array, 0, len(array) - 1, 8)
print binary_search_min(array, 0, len(array) - 1, 14)
print binary_search_min(array, 0, len(array) - 1, 15)
print binary_search_min(array, 0, len(array) - 1, 16)


