## 出错点在设置初值upper=len(nums)而不是len(nums)-1.
## 核心点在于设置一个变量Left来控制二分法程序搜索数组左索引还是右索引

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, left=True):
            low = 0
            upper = len(nums)
            
            while low < upper:
                mid = (low + upper) // 2
                if nums[mid] == target and left:
                    upper = mid
                    continue
                elif nums[mid] == target and not left:
                    low = mid + 1
                    continue
                elif nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    upper = mid
                
            return low
        
        if target not in nums:
            return [-1,-1]
        else:
            return [binary_search(nums,target, True),binary_search(nums,target, False)-1]