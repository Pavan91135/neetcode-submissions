class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        topk = []
        for i in nums:
            hashmap[i] = hashmap.get(i,0)+1

        freq = sorted(hashmap, key=hashmap.get, reverse=True)[:k]
        return freq