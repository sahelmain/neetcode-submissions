class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lengthS = len(s)
        lengthT = len(t)

        if lengthS != lengthT:
            return False
        sortedS = sorted(s)
        sortedT = sorted(t)
        for i in range(lengthS):
            if sortedS[i] != sortedT[i]:
                return False
        return True
