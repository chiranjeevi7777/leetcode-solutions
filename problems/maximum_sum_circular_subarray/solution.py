class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_max = max_num = nums[0]
        current_min = min_num = nums[0]
        total = sum(nums)

        for num in  nums[1:]:
            current_max = max(num, current_max + num)
            max_num = max(max_num, current_max)

            current_min = min(num, current_min + num)
            min_num = min(min_num, current_min)

        if max_num < 0:
            return max_num
        circular_sum = total - min_num

        return max(circular_sum, max_num)