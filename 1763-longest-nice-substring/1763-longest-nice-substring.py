class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s)<2:
            return ""
        uVal = set(s)
        for i,val in enumerate(s):
            if val.swapcase() not in uVal:
                r1 = self.longestNiceSubstring(s[0:i])
                r2 = self.longestNiceSubstring(s[i+1:])
                
                if len(r2)>len(r1):
                    return r2
                else:
                    return r1
        return s
        
            