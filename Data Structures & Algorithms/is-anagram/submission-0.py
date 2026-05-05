class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram
        s = sorted(s)
        t = sorted(t)
        return s == t