class Solution(object):
    nums = [3,3]
    target = 6
    def twoSum(self,nums, target):
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return [j,i]
                    
        return []
solution = Solution()
result = solution.twoSum(solution.nums,solution.target)
print(result)    