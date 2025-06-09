class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        numbers = list(range(1, n+1))
        numbers.sort(key=str)
        return numbers