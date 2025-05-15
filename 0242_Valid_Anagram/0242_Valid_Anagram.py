"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        return countS == countT
    
sol = Solution()
result = sol.isAnagram("anagram", "nagaram")
print(result)


"""
Loop Iteration
i = 0
s[0] = 'a'
t[0] = 'n'

countS['a'] = 1 + countS.get('a', 0) → 1 + 0 = 1
countT['n'] = 1 + countT.get('n', 0) → 1 + 0 = 1

countS = {'a': 1}, countT = {'n': 1}
<--------------------------->

i = 1
s[1] = 'n'
t[1] = 'a'
countS['n'] = 1 + countS.get('n', 0) → 1 + 0 = 1
countT['a'] = 1 + countT.get('a', 0) → 1 + 0 = 1
countS = {'a': 1, 'n': 1}, countT = {'n': 1, 'a': 1}
<--------------------------->

i = 2
s[2] = 'a'
t[2] = 'g'

countS['a'] = 1 + countS.get('a', 1) → 1 + 1 = 2
countT['g'] = 1 + countT.get('g', 0) → 1 + 0 = 1
countS = {'a': 2, 'n': 1}, countT = {'n': 1, 'a': 1, 'g': 1}
<--------------------------->
Continue...


"""