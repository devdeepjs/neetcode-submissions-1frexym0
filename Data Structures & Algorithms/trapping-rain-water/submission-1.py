class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0 , len(height)-1
        ans = 0 
        maxL,maxR = height[l],height[r]
        while (l<r):
            if maxL<maxR:
                l+=1
                maxL = max(height[l],maxL)
                ans+=maxL-height[l]
            else : 
                r-=1
                maxR= max(height[r],maxR)
                ans+=maxR-height[r]
        return ans              
            