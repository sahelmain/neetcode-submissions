class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num] = 1
        for n, c in count.items():
            frequency[c].append(n)

        result = []
        for i in range(len(frequency)-1, 0, -1):
            for number in frequency[i]:
                result.append(number)
                if len(result) == k:
                    return result