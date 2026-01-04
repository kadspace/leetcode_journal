# Engineering Journal: Group Anagrams & Hashing Strategy

## Challenge
Group a list of strings where each group contains anagrams of the same word.

### Approach
* **Sorting (Naive):** Sort every string ($N \cdot K \log K$). Slow for long strings.
* **Counter Strategy:** Use character counts as the key.
    * *Issue:* `frozenset(Counter(s))` only stores keys (letters), losing counts.
    * *Fix:* Use `frozenset(Counter(s).items())` to include counts.

### Complexity
* **Time:** $O(N \cdot K)$ where $N$ is number of strings, $K$ is max length.
* **Space:** $O(N \cdot K)$ to store groups.

### Key Concepts
* **Dict Keys:** Must be immutable. Use `tuple` for ordered, `frozenset` for unordered.
* **defaultdict:** Avoids manual existence checks.

### Solution
```python
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
```
