# -*- encoding: utf-8 -*-
"""
@File    : 94.py
@Time    : 2019-11-03 16:01
@Author  : ikukaku
@Email   : 1073258077@qq.com

给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import json
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return exec_main(root)


def exec_main(root):
    result = []
    if root is not None:
        left_result = exec_main(root.left)
        left_result.append(root.val)
        right_result = exec_main(root.right)
        for i in left_result:
            result.append(i)
        for i in right_result:
            result.append(i)
    return result


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    while True:
        try:
            line = raw_input().strip()
            root = stringToTreeNode(line)  # 将题目中的输入样例初始化为TreeNode结构

            ret = Solution().inorderTraversal(root)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
