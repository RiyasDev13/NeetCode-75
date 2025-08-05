class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,nums):
        rob1 = 0
        rob2 = 0

        for num in nums:
            newrob = max(rob1+ num,rob2)
            rob1 = rob2
            rob2 = newrob
        return rob2
        
