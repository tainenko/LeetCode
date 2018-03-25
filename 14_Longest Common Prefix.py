'''
Write a function to find the longest common prefix string amongst an array of strings.


'''


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for idx, word in enumerate(zip(*strs)):
            if len(set(word)) > 1:
                return strs[0][:idx]
        return ''


