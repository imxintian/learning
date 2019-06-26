class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 用len()方法取得nums列表长度
        n = len(nums)
        # 创建一个空字典
        d = {}
        for i in range(n):
            a = target - nums[i]
            # 字典d中存在nums[x]时
            if nums[i] in d:
                return d[nums[i]], i
            # 否则往字典增加键/值对
            else:
                d[a] = i
        # 边往字典增加键/值对，边与nums[x]进行对比


if __name__ == '__main__':
    so = Solution
    so.twoSum(nums=[1,2,3,4,5,6],target=5)
