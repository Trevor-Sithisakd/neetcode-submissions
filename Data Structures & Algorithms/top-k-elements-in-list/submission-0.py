class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k most frequent 
        # case 1 k = 1
        # how to find the most frequent get dictionary then count each occurence key: num value: count 
        # top k find the highest value then the next highest value till k
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)
        return sorted(d, key=lambda r: d[r], reverse=True)[:k]