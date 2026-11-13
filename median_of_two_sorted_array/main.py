class Solution(object):
    ## Best solution
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        n = len(nums)

        if n % 2:
            return nums[n // 2]

        return (nums[n // 2 - 1] + nums[n // 2]) / 2.0

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sortedArray = []
        nums1_count = 0
        nums2_count = 0
        while nums1_count < len(nums1) and nums2_count < len(nums2):
            if nums1[nums1_count] < nums2[nums2_count]:
                sortedArray.append(nums1[nums1_count])
                nums1_count += 1
            else:
                sortedArray.append(nums2[nums2_count])
                nums2_count += 1

            # Append any remaining elements once one array is exhausted
        sortedArray.extend(nums1[nums1_count:])
        sortedArray.extend(nums2[nums2_count:])

        total_len = len(sortedArray)
        mid_index = total_len // 2

        if total_len % 2 == 0:
            return (sortedArray[mid_index] + sortedArray[mid_index - 1]) / 2.0
        else:
            return float(sortedArray[mid_index])

if __name__ == "__main__":
    s = Solution()

    test_c_1_nums1 = [1, 3]
    test_c_1_nums2 = [2]
    print(s.findMedianSortedArrays(test_c_1_nums1, test_c_1_nums2))

    test_c_2_nums1 = [1, 2]
    test_c_2_nums2 = [3, 4]
    print(s.findMedianSortedArrays(test_c_2_nums1, test_c_2_nums2))