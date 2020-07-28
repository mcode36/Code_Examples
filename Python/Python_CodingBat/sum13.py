def sum13(nums):
  '''
  Return the sum of the numbers in the array, returning 0 for an empty array.
  Except the number 13 is very unlucky, so it does not count and numbers that
  come immediately after a 13 also do not count.
  https://codingbat.com/prob/p167025
  '''
  sum = 0
  i = 0
  while i < len(nums):
    if nums[i] != 13:
      sum = sum + nums[i]
      i = i + 1
    else:
      i = i + 2
      continue
  return sum

## Test
sum13([1, 2, 2, 1])             # 6	
sum13([1, 1])                   # 2	
sum13([1, 2, 2, 1, 13])         # 6	
sum13([1, 2, 13, 2, 1, 13])     # 4	
sum13([13, 1, 2, 13, 2, 1, 13]) # 3
sum13([])                       # 0
sum13([13])                     # 0
sum13([13, 13])                 # 0
sum13([13, 0, 13])              # 0
sum13([13, 1, 13])              # 0	
sum13([5, 7, 2])                # 14	
sum13([5, 13, 2])               # 5	
sum13([0])                      # 0
sum13([13, 0])                  # 0
