class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        W = 0
        for R in range(1, len(nums)):
            if nums[W] != nums[R]:
                W += 1
                nums[W] = nums[R]
        return W+1

        