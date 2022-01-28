class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ''
        min_len = len(min(strs, key=len))
        for i in range(min_len):
            count = 0
            for j in strs:
                if j[i]==strs[0][i]:
                    count += 1
            if count==len(strs):
                lcp += strs[0][i]
            else:
                break

        return lcp