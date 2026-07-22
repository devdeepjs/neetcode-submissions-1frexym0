class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sum = nums[0] if nums[0]>0 else 0 
        for i in range(1,len(nums),1):
            sum+=nums[i]
            ans = max(ans,sum)
            if (sum<=0):
                sum=0
        return ans        

        