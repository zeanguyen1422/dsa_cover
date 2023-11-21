
grid = [
  ["O","E","O","O"],
  ["E","O","W","E"],
  ["O","E","O","O"]
]

def maxKilledEnemies(grid):
  if len(grid) == 0 or len(grid[0]) == 0:
          return 0
  row = len(grid)
  col = len(grid[0])


  left = [[0 for _ in range(col)] for _ in range(row)]
  right = [[0 for _ in range(col)] for _ in range(row)]
  top = [[0 for _ in range(col)] for _ in range(row)]
  bottom = [[0 for _ in range(col)] for _ in range(row)]

  # loop từ trái qua phải
  for i in range(row):
    enemy_defeat = 0 
    for j in range(col):
      if grid[i][j] == "W":
        enemy_defeat = 0 
      elif grid[i][j] == "E":
        enemy_defeat += 1
      left[i][j] = enemy_defeat


  for i in range(row):
    enemy_defeat = 0 
    for j in range(col -1, -1, -1):
      if grid[i][j] == "W":
        enemy_defeat = 0
      elif grid[i][j] == "E":
        enemy_defeat += 1
      right[i][j] = enemy_defeat
 

  for j in range(col):
    enemy_defeat = 0 
    for i in range(row):
      if grid[i][j] == "W":
        enemy_defeat = 0
      elif grid[i][j] == "E":
        enemy_defeat += 1
      top[i][j] = enemy_defeat

  for j in range(col):
    enemy_defeat = 0 
    for i in range(row -1, -1, -1):
      if grid[i][j] == "W":
        enemy_defeat = 0
      elif grid[i][j] == "E":
        enemy_defeat += 1
      bottom[i][j] = enemy_defeat

  enemy = 0 

  for i in range(row):
    for j in range(col): # cái loop thứ 2 loop trước 
      if grid[i][j] == "O":
        enemy = max(enemy, left[i][j] + right[i][j] + bottom[i][j] + top[i][j])
  return enemy


print(maxKilledEnemies(grid))



