class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums)-1
        ans = 1e5
        while l<=r:
            # sorted pit 
            if (nums[l]<nums[r]):
                ans = min(ans,nums[l])
                break

            m = l + (r-l)//2
            if (nums[m]>=nums[l]):
                ans = min(ans,nums[l])
                l = m + 1 
            else : 
                ans = min(ans,nums[m])
                r = m -1 
        return ans            


        