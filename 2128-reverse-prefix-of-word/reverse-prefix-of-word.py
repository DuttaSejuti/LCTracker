class Solution:
    def get_the_index(self, word: str, ch: str) -> int:
        return word.find(ch)

    def reverse_the_prefix(self, word: List[str], idx: int) -> str:
        l, r = 0, idx

        while l <= r:
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1
        
        return ''.join(word)

    def reversePrefix(self, word: str, ch: str) -> str:
        # find the index of the ch
        idx = self.get_the_index(word, ch)

        # if the ch doesn't exist in the word, return the given word
        if idx == -1:
            return word

        # pass the string as a list to able to do re-assignment like s[l] = s[r]
        return self.reverse_the_prefix(list(word), idx)
