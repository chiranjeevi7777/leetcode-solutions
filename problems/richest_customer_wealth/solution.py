class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for customer in accounts:
            rowsum = sum(customer)
            maxWealth = max(maxWealth, rowsum)
        return maxWealth


        