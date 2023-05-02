# 844. Backspace String Compare

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

def backspaceCompare(self, s: str, t: str) -> bool:
    sRes, tRes = "", ""
    sPointer, tPointer = len(s) - 1, len(t) - 1
    backCounter = 0
    while sPointer >= 0:
        if s[sPointer] == "#":
            backCounter += 1
        elif s[sPointer] != "#" and backCounter == 0:
            sRes = s[sPointer] + sRes
        else:
            backCounter -= 1
        sPointer -= 1
    backCounter = 0
    while tPointer >= 0:
        if t[tPointer] == "#":
            backCounter += 1
        elif t[tPointer] != "#" and backCounter == 0:
            tRes = t[tPointer] + tRes
        else:
            backCounter -= 1
        tPointer -= 1
    return sRes == tRes