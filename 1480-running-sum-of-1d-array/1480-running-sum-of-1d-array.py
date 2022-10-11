class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cSum=0
        res=[]
        for i in nums:
            cSum+=i
            res.append(cSum)
        return res