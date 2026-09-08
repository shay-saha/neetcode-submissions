class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        alreadyseen = {}
        for i, v in enumerate(nums):
            complement = target - v
            if complement in alreadyseen:
                return [alreadyseen[complement],i]
            alreadyseen[v] = i
        #new list of already seen elements so 1 iteration in total, checks if the complement needed for each number has already been seen and naturally that will be a lower index. otherwise add number to alreadyseen 