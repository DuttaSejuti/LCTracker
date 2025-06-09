class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = list()
        curr = 1

        #as we want to generate n numbers
        for _ in range(n):
            result.append(curr)
            #go deeper
            if curr*10 <= n:
                curr *= 10
            #go to next childen
            elif curr % 10 != 9 and curr + 1 <=n:
                curr += 1
            else:
                #find next root node
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr += 1
        return result


