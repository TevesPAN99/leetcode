class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # 键是值，值是下标
        
        for i, num in enumerate(nums):
            complement = target - num   # 我要找的"另一半"
            
            if complement in seen:
                # 找到了！返回两个下标
                return [seen[complement], i]
            
            # 没找到，把当前数和它的下标存进字典
            seen[num] = i