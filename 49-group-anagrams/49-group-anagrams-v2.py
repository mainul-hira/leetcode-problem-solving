class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_angrams = {}
        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in group_angrams:
                group_angrams[sorted_word] = []
            
            group_angrams[sorted_word].append(word)
        return list(group_angrams.values())