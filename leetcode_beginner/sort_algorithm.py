




def sort(array):

    for index in range(1, len(array)):

        value = array[index]
        i = index - 1


        while i>=0 and value > array[i]:
            array[i + 1] = array[i] # swap variable
            array[i] = value    # swap trái bằng phải, dùng array[i + 1] ko đuọc vì array[i + 1] ở trên mới đổi value rồi 
            i = i - 1 

a = [1, 3, 2, 5, 9, 9, 8, 7]
sort(a)

print(a)









