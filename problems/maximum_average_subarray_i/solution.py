class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = 0
        for i in range(k):
            window += nums[i]
        answer = window
        for i in range(k, len(nums)):
            window += nums[i]
            window -= nums[i - k] 

            answer = max(answer, window)
        return answer / k
