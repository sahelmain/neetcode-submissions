class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        freq = [[] for i in range(len(nums) + 1)]


        for num in nums:
            if num in dict1:
                dict1[num]+=1
            else:
                dict1[num] = 1
        
        for num, count in dict1.items():
            freq[count].append(num)

        result = []
        for i in range(len(nums), 0, -1):
            for number in freq[i]:
                result.append(number)
                if len(result) == k:
                    return result
                