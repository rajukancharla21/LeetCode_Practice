class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tSum=sum(nums)
        cSum=0
        for idx,val in enumerate(nums):
            tSum-=val
            if cSum==tSum:
                return idx
            cSum+=val
        return -1
            
        