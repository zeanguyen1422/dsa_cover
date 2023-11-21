                              #3 (index col)
M = [ 	   [ 'a', 'c',  'd', 'r'],
           [ 'q', 'h',  'i', 'j'],
           [ 'w', 'm',  'n', 'o'],
           [ 'e', 'b',  's', 'v']   #row index 3
           ]



row = len(M)
column = len(M[0])




#upper anti-diagonal        r i m e     d h w c q a 
i = 0
while(i < column or i < row):
    x = 0
    y = column - i - 1
    while(x < row and y >= 0):
        print(M[x][y])
           
        x+=1
        y-=1
    i+= 1


#lower anti-diagonal    r i m e     j n b o s v

i = 0
while(i < column or i < row):
    x = i
    y = column - 1
    while(x < row and y >= 0):
        print(M[x][y])
            
        x+=1
        y-=1
    i+=1