class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for i in s:
            s_dict[i] = s_dict.get(i, 0)+1
        for j in t:
            # if j not in s_dict:
            #     return False
            s_dict[j] = s_dict.get(j, 0)-1
            if s_dict[j]==0:
                del s_dict[j]
        return False if s_dict else True
        
        
        