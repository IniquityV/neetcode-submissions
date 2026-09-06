class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a hashmap [key:value]
        hashmap = {}
        complement = 0
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[nums[i]] = i