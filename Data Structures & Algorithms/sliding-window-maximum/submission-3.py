class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        l , r = 0 , 0
        ans = []
        for r in range(len(nums)):
            while dq and dq[-1]<nums[r]:
                  dq.pop()
            dq.append(nums[r])    

            if (r-l+1==k):
                ans.append(dq[0])
                if (dq[0]==nums[l]):
                    dq.popleft()
                l+=1
        return ans        




        