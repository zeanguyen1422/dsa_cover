

#           4 cột 3 rows
matrix = [ [1,2,3, 4],
           [6, 7, 8, 9],
           [10, 11, 12, 13]
          ]
            #   0 1 2 3
            # 0
            # 1
            # 2

def spiralOrder(matrix):

    if not matrix:
                return []

    rows, cols = len(matrix), len(matrix[0])

    top, bottom = 0, rows-1 # theo index

    left, right = 0, cols-1 # theo index

    # vừa lấy index vừa lấy theo nghĩa row với column luôn á 

    result = []  
    
    while len(result) < rows * cols:

        for i in range(left, right + 1): # dcmm
            result.append(matrix[top][i]) # top là hàng row 0, i loop từ left tới right 
        top += 1 # top nhích xuống
        
        for i in range(top, bottom + 1):
            result.append(matrix[i][right]) # right <==> column
        right -= 1 # lùi lại
        
        if top <= bottom:  #oke oke         #dcmmm
            for i in range(right, left-1, -1): # left trừ 1 để nó loop tới số 0 
                result.append(matrix[bottom][i])  # append hết cái bottom mà nó loop từ right tới left theo cái i 
            bottom -= 1 # nhích lên
        
        if left <= right: # oke oke 
            for i in range(bottom, top-1, -1): #traverse lên 
                result.append(matrix[i][left]) # append hết cái left 
            left += 1 # nhích qua phải 

        # nó loop hết cái while luôn 
    
    return result

print(spiralOrder(matrix))