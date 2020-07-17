# coding:utf-8
class Solution:
    def searchInsert(self, nums, target):
        #暴力搜索
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                i += 1
                if i == len(nums):
                    return i
            else:
                return i


    def SearchInsert(self, nums, target):
        #二分查找
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left