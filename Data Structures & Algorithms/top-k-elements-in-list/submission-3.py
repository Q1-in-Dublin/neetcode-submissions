from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Solving with heap without most_common k
        
        count = Counter(nums)

        freq = [[] for _ in range(len(nums)+1)]
        # [[], [], [], [], [], [], []]
        # [[], [], [], [], [], [], []]
        # [[], [], [], [], [], [], []]
        for num, count in count.items():
            freq[count].append(num)
            # [[], [1], [], [], [], [], []]
            # [[], [1], [2], [], [], [], []]
            # [[], [1], [2], [3], [], [], []]
        result = []
        #most frequent
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result