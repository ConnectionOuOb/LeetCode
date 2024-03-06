"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Constraints
        numElement = len(nums)

        if numElement < 2 or numElement > 10**4:
            return []

        if target < -10**9 or target > 10**9:
            return []

        # Main
        for i in range(numElement):
            # Constraints
            if nums[i] < -10**9 or nums[i] > 10**9:
                return []

            # Return answer
            for j in range(i+1, numElement):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []


if __name__ == "__main__":
    s = Solution()

    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([3, 2, 4], 6))
    print(s.twoSum([3, 3], 6))
