from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            # 创建长度26的计数数组
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            # list 不能做字典的 key，转成 tuple
            groups[tuple(count)].append(s)
        
        return list(groups.values())