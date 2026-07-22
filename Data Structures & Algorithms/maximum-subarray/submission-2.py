class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        ans = sum
        if (sum<=0):
            sum=0
        for i in range(1,len(nums),1):
            sum+=nums[i]
            ans = max(ans,sum)
            if (sum<=0):
                sum=0
        return ans        

        