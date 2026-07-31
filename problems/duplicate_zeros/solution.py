class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)

        i = len(arr) - 1
        j = len(arr) + zeros - 1
        while i >= 0:
            if arr[i] != 0:
                if j < len(arr):
                    arr[j] = arr[i]
                i -= 1
                j -= 1 
            else:
                if j < len(arr):
                    arr[j] = 0
                j -= 1
            
                if j < len(arr):
                    arr[j] = 0
                j -= 1
                i -= 1