class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num = []
        for i in range(len(nums)):
            pro = 1
            for j in range(len(nums)):
                if i != j:
                    pro = pro*nums[j]
            num.append(pro)
        return num