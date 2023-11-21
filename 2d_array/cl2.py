

                              #3 (index col)
M = [ 	   [ 'a', 'c',  'd', 'r'],
           [ 'q', 'h',  'i', 'j'],
           [ 'w', 'm',  'n', 'o'],
           [ 'e', 'r',  's', 'v']   #row index 3
           ]



row = len(M)
column = len(M[0])

#upper diagonal      a h n v c i o d j r 
i = 0
while(i < column or i < row):
    x = 0
    y = i
    while(x < row and y < column):
        print(M[x][y])
        x += 1
        y += 1
    i += 1
            
#lower anti-diagonal 	# a h n v q m s w r e
i = 0
while(i < column or i < row):
    x = i  #swap
    y = 0  #swap 
    while(x < row and y < column):
        print(M[x][y])
            
        x+=1
        y+=1
    i+=1