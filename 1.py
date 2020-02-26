# -*- encoding: utf-8 -*-
"""
@File    : 1.py.py
@Time    : 2020-02-26 23:09
@Author  : ikukaku
@Email   : 1073258077@qq.com

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return main1(nums, target)


def main1(nums, target):
    helper = {}
    for index in xrange(len(nums)):
        if target-nums[index] in helper.keys():
            return [helper[target-nums[index]], index]
        else:
            helper.setdefault(nums[index], index)


if __name__ == '__main__':
    print main1([2,7,11,15], 9)