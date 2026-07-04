# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# gonna start with using a hash map to keep track of letters of s and their freqnecy. then decrement them as we loop thru t.
# O(2n) = O(n) I believe bcuz looping thru s and t only once each.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        counter = {}

        if len(s) != len(t): # forgot this when initially testing / running, chatgpt helped
            return False

        for letter in s:
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1
        for letter in t:
            if letter in counter:
                counter[letter] -= 1
                if counter[letter] < 0:
                    return False
            else:
                return False
        return True
    

# it's really ugly actually, for a known sequential list of items u can do the ord() method

sol = Solution()
f = sol.isAnagram

tests = [
    "anagram", "nagaram",
    "rat", "car",
    "listen", "silent",
    "a", "ab",
    "cass", "sacs"
]

print(f"{'s':<12} {'t':<12} output")
print("-" * 32)

for i in range(0, len(tests), 2):
    s = tests[i]
    t = tests[i + 1]
    print(f"{s:<12} {t:<12} {f(s, t)}")