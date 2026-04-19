class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        index = {}
        for i ,v in enumerate(nums):
            if target - v in seen:
                return [index[target-v],i]
            index.setdefault(v,i)
            seen.add(v)
        return [0,0]    