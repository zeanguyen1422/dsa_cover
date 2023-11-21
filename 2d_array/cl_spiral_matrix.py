


#           4 cột 3 rows
matrix = [ [1,2,3, 4],
           [6, 7, 8, 9],
           [10, 11, 12, 13]
          ]
            #   0 1 2 3
            # 0
            # 1
            # 2

# clm làm được rồi 

def spiralOrder(matrix):

	col = len(matrix[0])
	row = len(matrix)

	left = 0
	right = col - 1

	bottom = row - 1 	# theo index và xem bottom như rwo ở dưới 
	top = 0 

	# append hết top, loop trái qua phải 		# top là row đầu tiên á 

	result = []

	while len(result) < row * col:

		for i in range(left, right + 1 ):
			result.append(matrix[top][i])
		top += 1 		# nhảy xuống 

		for i in range(top, bottom + 1): # append hết cái right, right là col cuối index 
			result.append(matrix[i][right])
		right -= 1  # lùi lại 


		if top <= bottom:

			for i in range(right, left-1, -1):
				result.append(matrix[bottom][i])
			# bottom nhích lên 
			bottom -= 1

		if left <= right:

			for i in range(bottom, top-1, -1): # loop hết cái left tới right
				result.append(matrix[i][left])
			left += 1 # nhích qua phải 

	return result 

print(spiralOrder(matrix))