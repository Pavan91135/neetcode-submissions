class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = {}
        ya = False
        for i in range(n):
            if nums[i] in seen:
                ya = True
                return ya
            else:
                seen[nums[i]] = i
        return ya
           
        
