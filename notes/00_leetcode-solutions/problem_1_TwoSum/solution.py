class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hash table
        #建立一個空的字典
        seen = {} 
        #邊走邊檢查,要記得讓i跑到最後一個元素
        for i in range(len(nums)): 
            x = nums[i]
            complement = target - x
            if complement in seen:
                return [seen[complement], i]
            seen[x] = i
