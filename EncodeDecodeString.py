from typing import List


class Solution:

    def encode(strs: List[str]) -> str:
        res = ""
        # Numerical length + '#' + string itself
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    # Ex. 3#abc4#abcd
    def decode(s: str) -> List[str]:
        res = []
        i = 0
        # Outer loop runs from 0 to n, inside each iteration we use another var and set it equal to current index
        # Increment j until we see the character '#', then we can slice s[i:j] to get the length of the string then
        # reassign i to index of '#' + 1 which is start of the string, and set j to i + length.
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
    print(decode(s='3#abc4#abcd'))