class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print(nums, target)
        # brute force method
        for i in range(len(nums)):
            print(f"i = {i}")            
            for x in nums[(i + 1):]:
                print(f"x = {x}")
                if nums[i] + x == target:
                    print("Found it")
                    return [i, nums.index(x)]
        return [-1, -1]


solution = Solution()
print(solution.twoSum([2,7,11,15], 9)) # expecting [0, 1]
print(solution.twoSum([3, 2, 4], 6)) # expecting [1, 2]
print(solution.twoSum([3, 3], 6)) # expecting [0, 1] but there's a bug that returns [0, 0]