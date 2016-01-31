class Solution(object):
    #divide and conquer
    def myPow_stupid(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        powerset = {1:x}
        def rec(num, exp):
            
            if exp not in powerset.keys():
                powerset[exp] = rec(num,exp//2) * rec(num, (exp+1)//2)
                
            return powerset[exp]
        if n<0:
            val = rec(x,-n)
            return 1./val
        return rec(x, n)

    def myPow(self,x,n):
        '''
		Smarter implementation
		'''
        if n==1:
            return x
        if n==0:
            return 1    
        if n==-1:
            return 1./x
        return self.myPow(x*x, n//2)*[1,x][n%2]
