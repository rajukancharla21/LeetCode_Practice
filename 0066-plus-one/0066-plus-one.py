class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = ''.join(map(str,digits))
        return list(str(int(val)+1))
        