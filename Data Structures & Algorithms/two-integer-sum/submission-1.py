class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i in range(len(nums)):
            complement[target - nums[i]] = i
        for j in range(len(nums)):
            if nums[j] in complement and complement[nums[j]] != j:
                return sorted([j, complement[nums[j]]])