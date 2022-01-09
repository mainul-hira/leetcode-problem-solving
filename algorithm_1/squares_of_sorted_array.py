def sortedSquares(nums):
    new_list = [-4,-1,0,3,10]
    negative_list = []
    for i in new_list:
        if i<0:
            negative_list.append(abs(i))
    
    print(negative_list)
    square_list = [i*i for i in new_list]
    print(sorted(square_list))

sortedSquares(1)