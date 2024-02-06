class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_dict = dict()
        r_dict = dict()
        for m in magazine:
            m_dict[m] = m_dict.get(m, 0) + 1

        for r in ransomNote:
            r_dict[r] = r_dict.get(r, 0) + 1

        for r in ransomNote:
            if r not in m_dict or m_dict[r] < r_dict[r]:
                return False
        return True
