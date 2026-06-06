class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictionary1 = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for character in string: 
                count[ord(character) - ord("a")] += 1
            
            dictionary1[tuple(count)].append(string)
        
        return list(dictionary1.values())