class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first():
            l = 0
            r = len(nums) - 1
            answer = -1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    answer = mid
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return answer 
        def find_last():
            l = 0
            r = len(nums) - 1
            answer = -1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    answer = mid
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return answer 
        return [find_last(), find_first()]

