
array = [
[1, 2, 3, 4, 10],
[2, 2, 3, 4, 5],
[5, 2, 1, 4, 5],
[8, 2, 3, 4, 5],

]


column = len(array[0])
row = len(array)


# sum += row
sum_total = 0 
for i in range(row): 
	for j in range(column): # cái loop thứ 2 chạy trước 
		sum_total += array[i][j]
	print(sum_total)



# sum += column
sum_total = 0 
for j in range(column):
	for i in range(row): # cái loop thứ 2 chạy trước 
		sum_total += array[i][j] # loop cái row trước rồi loop cái column sau 
	print(sum_total)


