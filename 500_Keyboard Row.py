'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rset=list(map(set,['qwertyuiop','asdfghjkl','zxcvbnm']))
        res=[]
        for word in words:
            wset=set(word.lower())
            if any( wset <= row for row in rset):
                res.append(word)
        return res