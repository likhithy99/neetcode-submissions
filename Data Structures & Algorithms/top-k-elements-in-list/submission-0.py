class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
          if n in d:
            d[n] += 1
          else:
            d[n] = 1
        sorted_nums = sorted(d, key=lambda x: d[x], reverse=True)
        return sorted_nums[:k]
        
        