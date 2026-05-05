def lengthOfLongestSubstring(s: str) -> int:
        seen = set()
        left, right, longest = 0, 0, 0
        while(right < len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                longest = max(longest, len(seen))
                right += 1
            else:
                seen.remove(s[left])
                left += 1
        return longest