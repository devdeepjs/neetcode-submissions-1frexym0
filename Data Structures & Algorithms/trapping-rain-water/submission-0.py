class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [-1]*len(height)
        right_max = [-1]*len(height)

        left = height[0]
        for i in range(1,len(height)):
            if (height[i]<left):
                left_max[i] = left
            left = max(left,height[i])

        right= height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            if (height[i]<right):
                right_max[i] = right 
            right = max(right,height[i])

        ans = 0 
        print(left_max,right_max)
        for i in range(len(height)):
            if (left_max[i]==-1 or right_max[i]==-1):
                continue
            ans+=(min(left_max[i],right_max[i])-height[i])
        return ans                