def longestCommonPrefix(self, strs):
    if not strs:
        return ""
    shortest = min(strs,key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest

strs = ["flower","flow","flight"]

#https://qiita.com/ishishow/items/9c2075b2b08721d5f314https://qiita.com/ishishow/items/9c2075b2b08721d5f314