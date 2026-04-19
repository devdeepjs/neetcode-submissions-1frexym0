class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        seen = set(nums)
        ans = 0 
        for num in nums:
            ans = max(ans,func(mp,seen,num))
        return ans    


def func(mp: dict[int], seen : set(int),num):
        if num-1 in seen:
            func(mp,seen,num-1)
            mp[num] = mp[num-1]+1
        else :
            mp[num] = 1     
        return mp[num]

        
        