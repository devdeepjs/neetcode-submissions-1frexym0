class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0 
        stack = [] # pair (index, height)

        for i,h in enumerate(heights):
            start = i 
            while stack and stack[-1][1]>h:
                ans = max(ans,(i-stack[-1][0])*stack[-1][1])
                start = stack[-1][0]
                stack.pop()
            stack.append([start,h])  

        for i , h in stack:
            ans = max(ans,h*(len(heights)-i))
        return ans      
        