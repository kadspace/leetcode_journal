# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

from typing import List

# first thought was to create a dict where we can keep track of anagram letter combos, the tricky part is the duplicate letters.
# can be done with freezing a sorted list into a tuple and using that as the dict key, then the value of the elements is index of where they show up on the initial list

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # need a main lookup dict
        lookup = {}

        # for every elements in strs, lets turn it into a list of letters -> sort it -> freeze it as a tuple and use it as a key
        for word in strs:
            # turning the str into a list of letters-- i'll use list comprehension
            list_ = [l for l in word]
            # sort it (.sort() does NOT return the sorted list)
            list_.sort()
            # freeze it to a tuple
            tuple_ = tuple(list_)
            # try to find it in the lookup dict, if not available, create one
            if tuple_ in lookup:
                lookup[tuple_].append(word)
            else:
                lookup[tuple_] = [word] # make sure we are creating a list as the value, with one element (first occurance of this anagram)

        return [value for value in lookup.values()]
            

# gpt generated test cases
sol = Solution()
f = sol.groupAnagrams

tests = [
    ["eat", "tea", "tan", "ate", "nat", "bat"],
    [],
    [""],
    ["", ""],
    ["abc"],
    ["abc", "def", "ghi"],
    ["abc", "bca", "cab", "acb"],
    ["eat", "eat", "tea"],
    ["a", "aa", "aaa"],
    ["ab", "abb", "aab", "bab"]
]

print(f"{'strs':<45} output")
print("-" * 80)

for strs in tests:
    print(f"{str(strs):<45} {f(strs)}")