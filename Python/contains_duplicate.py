# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

from typing import List

# just wanna use a set for this one, let me look up the push and pops of that structure
# looks like I will need .add(x) and .remove(x) (this one errors out if item is missing, which is actually a "valid" case here)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set() # our main set
        for num in nums:
            try:
                s.remove(num)
                return True
            except KeyError:
                s.add(num)
        return False


# analysis:
# ok gpt is saying I did it weird lol, it is odd to use try and except but that was making sense to me. still time and space of O(n)
# better way to do it is use "if num in s" as the primary check in the main for loop, will do that next time

sol = Solution()
f = sol.containsDuplicate

tests = [
    [1, 2, 3, 1],
    [1, 2, 3, 4],
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
    [],
    [1],
    [0, 0],
    [-1, -2, -3, -1],
    [1000000, 1, 2, 3],
    [5, 5],
    [1, 2, 3, 4, 5, 6, 7]
]

print(f"{'nums':<45} output")
print("-" * 60)

for nums in tests:
    print(f"{str(nums):<45} {f(nums)}")