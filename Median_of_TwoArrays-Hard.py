class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        from numpy import median
        result  = nums1 + nums2
        return median(result)

#----From Scratch Method-----#
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n_num = nums1 + nums2
        n = len(n_num)
        n_num.sort()
        
        if n % 2 == 0:
            median1 = float(n_num[n//2])
            median2 = float(n_num[n//2 - 1])
            median = float((median1 + median2)/2)
        else:
            median = n_num[n//2]
        return median