class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLength = len(s)
        tLength = len(t)
        if (sLength == tLength):
            s_new = sorted(s)
            t_new = sorted(t)
            if s_new==t_new:
                return True 
            else:
                return False
        else:
            return False