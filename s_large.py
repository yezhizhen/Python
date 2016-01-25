def rec(start,end, height):
    count = 0
    #find largest and second largest
    large = -1
    s_large = -1
    l_i = start
    s_i = -1
    for i in range(start,end+1):
        if height[i]>large:
            large,s_large = height[i], large
            l_i,s_i = i,l_i
        elif height[i]>s_large:
                s_large = height[i]
                s_i = i
    return large,s_large, l_i, s_i