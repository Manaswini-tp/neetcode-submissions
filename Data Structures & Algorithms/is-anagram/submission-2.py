class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        if len(s)!=len(t):
            return False
        for c in s:
            if c in countS:
                countS[c]+=1
            else:
                countS[c]=1
        
        for c in t:
            if c in countS:
                countS[c]-=1
            else:
                countS[c]=-1
        
        for value in countS.values():
            if value != 0:
                 return False

        return True