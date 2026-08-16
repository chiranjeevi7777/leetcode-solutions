class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = 0
        count = {}
        answer = 0

        # First window
        for i in range(k):
            window += nums[i]
            count[nums[i]] = count.get(nums[i], 0) + 1

        if len(count) == k:
            answer = window

        # Slide the window
        for i in range(k, len(nums)):

            # Remove outgoing element
            outgoing = nums[i - k]
            window -= outgoing
            count[outgoing] -= 1

            if count[outgoing] == 0:
                del count[outgoing]

            # Add incoming element
            incoming = nums[i]
            window += incoming
            count[incoming] = count.get(incoming, 0) + 1

            # Check distinct
            if len(count) == k:
                answer = max(answer, window)

        return answer