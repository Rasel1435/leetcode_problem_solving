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
    
    
# another way 
from collections import Counter
class Soluation:
    def __init__(self, s: str, t: str) -> None:
        self.s = s
        self.t = t
    def isAnagram(self) -> bool:
        return sorted(self.s) == sorted(self.t)
        return Counter(self.s) == Counter(self.t)
        
if __name__ == '__main__':
    s = input()
    print(f'S: {s} ')
    t = input()
    print(f'T: {t} ')
    sol = Soluation(s, t)
    print(sol.isAnagram())