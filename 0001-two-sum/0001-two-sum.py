class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem={}
        for idx,val in enumerate(nums):
            diff = target-val
            if diff in mem:
                return [idx,mem[diff]]
            else:
                mem[val]=idx
        return[-1,-1]
        
        
            
        