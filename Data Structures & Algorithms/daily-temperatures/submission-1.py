class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        for i in range(len(temperatures)-1,-1,-1):
            while stack and stack[-1][0]<=temperatures[i]:
                stack.pop()
            result.append(0 if not stack else stack[-1][1]-i)
            stack.append([temperatures[i],i])
        return result[::-1]
        