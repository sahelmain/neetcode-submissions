class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)

        for number in nums:
            count[number] +=1
        
        sorted_keys = sorted(count, key = count.get, reverse = True)
        return sorted_keys[0:k]