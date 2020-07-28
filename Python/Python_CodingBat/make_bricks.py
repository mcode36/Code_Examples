'''
# method 1
def make_bricks(small, big, goal):
  possible = False
  i = 0
  for i in range(0,big+1):
    for j in range(0,small+1):
      # print(i,j,i*5+j)
      if i*5 + j == goal:
        possible = True
        break
    if possible:
      break
  return possible


# method 2
def make_bricks(small, big, goal):
  i = 0
  for i in range(0,big+1):
    for j in range(0,small+1):
      if i*5 + j == goal:
        return True
  return False
'''

# method 3
def make_bricks(small, big, goal):
    if goal % 5 == 0:
        if big >= goal/5 or big*5 + small >= goal:
            return True
        else:
            return False
    else:
        if big >= (goal-(goal%5))/5 and small >= goal%5:
            return True
        elif big < (goal-(goal%5))/5 and small >= goal-(big*5):
            return True
        else:
            return False
    
          

print(make_bricks(3, 1, 8))  # T
print(make_bricks(3, 1, 9))  # F
print(make_bricks(3, 2, 9))  # F
print(make_bricks(3, 2, 10)) # T
