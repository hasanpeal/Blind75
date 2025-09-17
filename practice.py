def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        l,r,m = 0, 0, 0
        while r < len(s):
            seen[s[r]] = 1 + seen.get(s[r], 0)
            while ((r - l + 1) - max(seen.values())) > k:
                seen[s[l]] -= 1
                l += 1
            m = max(m, r - l + 1)
            r += 1
        return m