class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minL = len(sorted(strs,key=len)[0])
        r=""
        stop=False
        for i in range(minL):
            for j in range(len(strs)-1):
                if(strs[j][i]!=strs[j+1][i]):
                    stop=True
                    break
            else:
                r+=strs[0][i]
            if stop:
                break
        return r
                
                    
            
        