def combinationSum(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def rec(ind,target, temp):
            for i in range(ind, len(candidates)):
                if target < candidates[i]:
                    break
                #base case
                elif target == candidates[i]:
                    res.append(temp+[target])
                else:
                    rec(i,target-candidates[i],temp+[candidates[i]])
        candidates.sort()
        #Find Sums 
        rec(0, target, [])
        return res

		
		
candidates = [ int(x) for x in input('Input the candidates set\n').split()]
target = int(input ('Input the target\n'))
res = combinationSum(candidates,target)

for r_ in res:
	print(r_)

input('Press Enter to Exit')
#exec(open('Combination_Sum.py').read())