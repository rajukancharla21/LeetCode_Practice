class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for idx, val in enumerate(nums):
            diff = target-val
            if diff not in mem:
                mem[val]=idx
            else:
                return [mem[diff],idx]
        return [-1,-1]
        
        
        
            
        