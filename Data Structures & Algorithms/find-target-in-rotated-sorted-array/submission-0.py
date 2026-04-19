class Solution:

    def binary_search(self,nums : List[int],target: int, l : int, r : int)->int:
        while(l<=r):
            m = l + (r-l)//2 
            if (nums[m]==target):
                return m 
            elif (nums[m]<target):
                l = m +1 
            else : 
                r = m - 1 
        return -1        

    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)-1
        index = 0 
        while(l<=r):
            if (nums[l]<=nums[r]):
                index = l if nums[l]<nums[index] else index 
            m = l + (r-l)//2 
            if (nums[m]>=nums[l]):
                index = l if nums[l]<nums[index] else index
                l = m + 1 
            else : 
                index = m if nums[m]<nums[index] else index 
                r = m - 1 
         
        print(index)
        ans_1 = self.binary_search(nums,target,0,index-1) 
        ans_2 = self.binary_search(nums,target,index,len(nums)-1)

        return ans_1 if (ans_1!=-1) else ans_2





        