
array = [
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
					# 2 x 5


]


# 		 0  1  2  3  4 
# 0 	[1, 2, 3, 4, 5],
# 1		[6, 7, 8, 9, 10],
#
col = len(array[0]) # 4
row = len(array) # 2




# left to right
i = 0
while(i < row): 
    j = 0
    while(j < col):
        print(array[i][j])
        j += 1
    i += 1
# attacking left
for i in range(row):
  for j in range(col):
    print(grid[i][j])
    
#right
for i in range(row):
  for j in range(column - 1, -1, -1):
    print(grid[i][j])

# up
for j in range(col):
	for i in range(row):  # loop thứ 2 chạy trước 
		print(array[i][j]) 




		# 0 0 1 0 0 1 1 1 

# bottom
for j in range(col):
	for i in range(row -1, -1, -1): 
		print(array[i][j]) 

	
