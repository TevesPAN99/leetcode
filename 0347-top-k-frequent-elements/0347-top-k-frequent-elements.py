class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}                    # ← 从这里开始写
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        sorted_keys = sorted(count, key=lambda x: count[x], reverse=True)
        return sorted_keys[:k]