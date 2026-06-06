class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lengthS = len(s)
        lengthT = len(t)

        if lengthS!=lengthT:
            return False

        s= sorted(s)
        t= sorted(t)
        
        if s == t: 
            return True

        return False