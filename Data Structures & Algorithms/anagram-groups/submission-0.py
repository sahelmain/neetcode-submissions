class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1 = defaultdict(list)

        for string in strs:
            alphabetCount = [0] * 26

            for character in string:
                alphabetCount[ord(character) - ord("a")]+=1
            
            dict1[tuple(alphabetCount)].append(string)

        return list(dict1.values())