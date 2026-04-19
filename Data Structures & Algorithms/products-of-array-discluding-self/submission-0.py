class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        mul = 1 
        for i in range(len(nums)):
            res[i] = mul
            mul*=nums[i]

        mul = 1 
        for i in range(len(nums)-1,-1,-1):
            res[i]*=mul
            mul*=nums[i]
            
        return res        



        