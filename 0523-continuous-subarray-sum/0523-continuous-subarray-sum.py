class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        h={0:0}
        c=0
        for i,v in enumerate(nums):
            c+=v
            if (c%k) not in h:
                h[c%k]=i+1
            elif h[c%k]<i:
                return True
        return False
                
        