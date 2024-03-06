"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        n1, n2 = len(nums1), len(nums2)
        for i in nums1:
            notFound = True

            for j in range(len(nums2)):
                if i <= nums2[j]:
                    nums2.insert(j, i)
                    notFound = False
                    break

            if notFound:
                notFound = True
                nums2.append(i)

        if nums2 == []:
            nums2 = nums1

        numElement = n1 + n2
        midNumber1 = int(numElement / 2)
        midNumber2 = int((numElement-1) / 2)

        return (nums2[midNumber1] + nums2[midNumber2]) / 2.0


if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
    print(s.findMedianSortedArrays([2], []))
    print(s.findMedianSortedArrays([1, 3], [2, 7]))
    print(s.findMedianSortedArrays([100001], [100000]))
    print(s.findMedianSortedArrays([1, 3, 4], [2]))
