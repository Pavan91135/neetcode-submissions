class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        topk = []
        for i in nums:
            hashmap[i] = hashmap.get(i,0)+1
        freq = sorted(list(hashmap.values()), reverse=True)

        for num, fre in hashmap.items():
            if fre in freq[0:k]:
                topk.append(num)
        return topk
        
        
        