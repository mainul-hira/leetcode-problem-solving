def sortedSquares(nums):
    new_list = [-4,-1,0,3,10]
    
    p_1 = 0
    p_2 = len(new_list)-1
    while p_1<p_2:
        if abs(new_list[p_1])<abs(new_list[p_2]) and abs(new_list[p_1])>abs(new_list[p_2-1]):
            new_list.insert(p_2-1, nums[p_1])
            new_list.pop(p_1)
            
    print(new_list)
    square_list = [i*i for i in new_list]
    print(sorted(square_list))

sortedSquares(1)