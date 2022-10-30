from math import floor
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            if i%2==0 and i%3==0:
                a.append(i)
        return 0 if a==[] else math.floor(sum(a)/len(a))
        