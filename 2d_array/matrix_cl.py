

                              #3 (index col)
matrix = [ [ 'a', 'c',  'd', 'r'],
           [ 'q', 'h',  'i', 'j'],
           [ 'w', 'm',  'n', 'o'],
           [ 'e', 'r',  's', 'v']   #row index 3
           ]

row = len(matrix)
column = len(matrix[0])



# thất sự là đéo có hiểu luôn 

for i in range(row):                        # a q c w h d e m i r 
    j = 0 
    while i >= 0 and j <= column:
        print(matrix[i][j])
        i = i - 1
        j = j + 1


for j in range(1, column):                          # r n j o s v 
    i = row - 1 # bắt đầu từ hàng row cuối 
    while i >= 0 and j <= column - 1:
        print(matrix[i][j])
        i = i - 1 
        j = j + 1


