def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        haveMap, needMap = {}, {}
        # res stores the indices of l, f for substring
        l, r, res, resLength = 0, 0, [-1, -1], float("inf")
        for c in t:
            needMap[c] = 1 + needMap.get(c, 0)
        have = 0
        # Need here is the total character. We only increment have if total count of a character is meet
        need = len(needMap)
        while r < len(s):
            curr = s[r]
            # Adding character on right to the hashmap
            haveMap[curr] = 1 + haveMap.get(curr, 0)
            # If we meet the total required number of certain character, we increment have
            if curr in needMap and haveMap[curr] == needMap[curr]:
                have += 1
            while have == need:
                if (r - l + 1) < resLength:
                    res = [l, r]
                    resLength = r - l + 1
                haveMap[s[l]] -= 1
                # If character of left is in need map and doesn't meet the total occurence then have -1
                if s[l] in needMap and haveMap.get(s[l]) < needMap.get(s[l]):
                    have -= 1
                l += 1
            r += 1
        l, r = res
        return s[l:r+1] if resLength != float("inf") else ""