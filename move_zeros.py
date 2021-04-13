class Solution(object):
    # Move any zeros in a list to the left while mataining the order of non-zero values
    def move_zeros(self, list):
        # check if there's more than one element in the list, return if there isn't
        if len(list) == 1:
            return
        zero_list = []
        for pos, x in enumerate(list):
            if x == 0:
                zero_list.append(x)
                list.pop(pos)
        return zero_list + list

if __name__ == '__main__':
    solution = Solution()
    arr1 = [0,34,5,6,0,9,0,2,5]
    arr2 = [15,1,5,0,6,0,0,12,0,29,5]
    print(solution.move_zeros(arr1))
    print(solution.move_zeros(arr2))