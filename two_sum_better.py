class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myHash = {}
        print(list(enumerate(nums)))
        for index, value in enumerate(nums):
            print(myHash, value, index)
            if target - value in myHash:
                return [myHash[target-value], index]
            myHash[value] = index

my_solution = Solution()
print(my_solution.twoSum([3,5,6,7,8], 11))