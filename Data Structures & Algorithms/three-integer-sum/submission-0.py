class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i,v in enumerate(nums):
            if v > 0 : 
                break
            if i>0 and v==nums[i-1]:
                continue

            target = v
            j = i+1
            k = len(nums)-1
            while j<k:
                if nums[j]+nums[k]+target<0:
                    j+=1
                elif nums[j]+nums[k]+target>0:
                    k-=1
                else : 
                    ans.append([target,nums[j],nums[k]])
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
        return ans           

        