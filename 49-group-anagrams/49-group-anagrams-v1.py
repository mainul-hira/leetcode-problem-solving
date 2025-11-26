class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_idx_set = set()
        char_count_list = []

        for idx, word in enumerate(strs):
            current_char_count = {}
            for ch in word:
                current_char_count[ch] = current_char_count.get(ch, 0) + 1
            
            char_count_list.append(current_char_count)
        
        group_anagrams = []

        for idx, val in enumerate(char_count_list):
            if idx in anagram_idx_set:
                continue
            
            anagrams = [strs[idx]]
            if idx == len(char_count_list)-1:
                group_anagrams.append(anagrams)
                continue
                
            for idx1, val1 in enumerate(char_count_list[idx+1:]):
                if val == val1:
                    anagrams.append(strs[idx+idx1+1])
                    anagram_idx_set.add(idx+idx1+1)
            
            group_anagrams.append(anagrams)
        return group_anagrams