# 49. Group Anagrams (Medium)
# Pattern: hash map with a canonical key
# Approach 1 (sorted key):  Time O(n * k log k)  Space O(n * k)
# Approach 2 (count key):   Time O(n * k)        Space O(n * k)
#   n = number of words, k = max word length
# Mistake / what I learned: (fill this in after you re-solve it from memory)

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Approach 1: the sorted word is the key. 'eat' -> 'aet'."""
        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)
        return list(groups.values())

    def groupAnagramsCount(self, strs: List[str]) -> List[List[str]]:
        """Approach 2: a 26-slot letter count is the key. Faster for long words."""
        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord("a")] += 1
            groups[tuple(count)].append(word)  # lists can't be dict keys; tuples can
        return list(groups.values())


if __name__ == "__main__":
    s = Solution()
    tests = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]
    norm = lambda g: sorted(sorted(x) for x in g)
    for strs, expected in tests:
        assert norm(s.groupAnagrams(strs)) == norm(expected)
        assert norm(s.groupAnagramsCount(strs)) == norm(expected)
    print("all tests passed")
