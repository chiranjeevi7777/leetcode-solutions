class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        W = 0
        for R in range(len(nums)):
            if nums[R] != 0:
                nums[W] = nums[R]
                W += 1
        for i in range(W, len(nums)):
            nums[i] = 0

        