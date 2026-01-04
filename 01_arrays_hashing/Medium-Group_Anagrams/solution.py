from collections import defaultdict, Counter
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            # key includes counts to handle duplicate chars e.g. "abb" vs "ab"
            key = frozenset(Counter(s).items())
            groups[key].append(s)
            
        return list(groups.values())
