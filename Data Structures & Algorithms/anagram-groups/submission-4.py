class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict1 = defaultdict(list)

        for string in strs:
            count = [0] * 26 # a,b,c... z, index 0-25

            for character in string: 
                count[ord(character) - ord("a")]+=1

            dict1[tuple(count)].append(string)
        
        return list(dict1.values())