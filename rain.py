def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height)<=2:
        return 0
    return rec(0,len(height)-1, height)
    
def rec(start,end, height):
    if start +1 >= end:
        return 0
    def s_large():
        #find largest and second largest
        large = -1
        s_large = -1
        l_i = start
        s_i = -1
        for i in range(start,end+1):
            if height[i]>large:
                large,s_large = height[i], large
                l_i,s_i = i,l_i
            elif height[i] > s_large:
                    s_large = height[i]
                    s_i = i
        return l_i, s_i       
    count = 0
    #find largest and second largest(can be duplicate)
    l_i,s_i = s_large()
    print('start:{:d},   end:{:d},   l_i:{:d},   s_i{:d}'.format(start,end,l_i,s_i))
    input('Press Enter to continue')
    second_large = height[s_i]
    if l_i > s_i:
        l_i,s_i = s_i,l_i
    #now, we have changed the position to make l_i smaller
    #loop through region between the two
    for i in range(l_i+1,s_i):
        count +=  second_large - height[i]
    count += rec( start, l_i,height) + rec(s_i,end,height)
    
    return count