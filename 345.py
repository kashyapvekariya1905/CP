class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowel_positions = [i for i, char in enumerate(s) if char in vowels]
        vowel_chars = [s[i] for i in vowel_positions]
        vowel_chars.reverse()
        s_list = list(s)
        for pos, char in zip(vowel_positions, vowel_chars):
            s_list[pos] = char
        return ''.join(s_list)