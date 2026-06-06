class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict1 = defaultdict(list)

        for stringWord in strs:
            count = [0] * 26

            for character in stringWord:
                count[ord(character) - ord("a")]+=1
            
            dict1[tuple(count)].append(stringWord)

        return list(dict1.values())