
arr = [1, 2, 5, 8, 2, 1, 3]
def okay(arr):
    
    if len(arr) < 3:
        return 0 

    # đcmm

    lenght = 0 
    direction = 1 
    cur_len = 0

    for i in range(1, len(arr)):

        prev_val = arr[i - 1]
        next_val = arr[i]

        if direction == 1:
            if next_val > prev_val:
                cur_len += 1 if cur_len > 0 else 2
            elif next_val < prev_val and cur_len > 0:
                direction = -1 # set xuống
                cur_len += 1
                lenght = max(lenght, cur_len)
            if prev_val == next_val:
                cur_len = 0 
                

        elif direction == -1:
            if next_val > prev_val:
                cur_len = 2
                direction = 1
            if next_val < prev_val:
                cur_len += 1 
                lenght = max(lenght, cur_len)
            if prev_val == next_val:
                #direction = 1
                cur_len = 0 
    return lenght
        
print(okay(arr))