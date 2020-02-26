# -*- encoding: utf-8 -*-
"""
@File    : 345.py.py
@Time    : 2020-01-12 01:57
@Author  : ikukaku
@Email   : 1073258077@qq.com

编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        return main1(s)


def main1(input_str):
    if not input_str:
        return ''
    s = list(input_str)
    helper = ['a', 'o', 'e', 'i', 'u']
    end = len(s) - 1
    start = 0
    while start <= end:
        if s[start] in helper or s[start].lower() in helper:
            if s[end] in helper or s[end].lower() in helper:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
                continue
        else:
            start += 1
        if s[end] in helper or s[end].lower() in helper:
            if s[start] in helper or s[start].lower() in helper:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
                continue
        else:
            end -= 1

    return "".join(s)


if __name__ == '__main__':
    print main1('ai')
