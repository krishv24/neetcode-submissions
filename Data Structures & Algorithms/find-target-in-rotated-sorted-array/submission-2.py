class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        minimum=9999999
        mid=(left+right)//2
        if nums[mid] < minimum:
            minimum=nums[mid]
            print("minimum",minimum)
        if nums[mid]==target:
                return mid
        def binsearch(nums,left,right):
            mid = (left + right) // 2

            if left > right:
                return -1

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # left half is sorted

                if nums[left] <= target < nums[mid]:
                    return binsearch(nums, left, mid - 1)
                else:
                    return binsearch(nums, mid + 1, right)

            else:
                # right half is sorted

                if nums[mid] < target <= nums[right]:
                    return binsearch(nums, mid + 1, right)
                else:
                    return binsearch(nums, left, mid - 1)
        return binsearch(nums,left,right)
