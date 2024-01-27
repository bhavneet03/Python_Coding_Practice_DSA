def binary_search(low, high):
			if low >= high: return low
			
			mid = (low + high) // 2
			if isBadVersion(mid):
				if isBadVersion(mid-1) == False: return mid # first bad item
				return binary_search(low, mid-1) # keep searching in the first half intervals
			else:
				return binary_search(mid+1, high) # keep searching in the second half intervals

		return binary_search(1,n)
		

 def firstBadVersion(self, n):
        if n==1: 
            return 1;
        begin=1
        end=n
        while begin<end:
            mid=begin+(end-begin)/2
            if isBadVersion(mid): end=mid
            else: begin=mid+1
        return int(begin)
		
		
		
class Solution(object):
    def searchInsert(self, nums, target):
        mid = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return right + 1
        
        