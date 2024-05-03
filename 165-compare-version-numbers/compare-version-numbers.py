class Solution:
    def padd_the_smaller_with_zeros(self, new_list_1: List[str], new_list_2: List[str]) -> Tuple[List[int], List[str]]:
        l1, l2 = len(new_list_1), len(new_list_2)

        if l1 < l2:
            diff = l2-l1
            for _ in range(diff):
                new_list_1.append('0')

        elif l1 > l2:
            diff = l1-l2
            for _ in range(diff):
                new_list_2.append('0')
        
        return new_list_1, new_list_2

    def compareVersion(self, version1: str, version2: str) -> int:
        new_list_1 = version1.split('.')
        new_list_2 = version2.split('.')

        new_list_1, new_list_2 = self.padd_the_smaller_with_zeros(new_list_1, new_list_2)

        l = len(new_list_1)

        for i in range(l):
            if int(new_list_1[i]) < int(new_list_2[i]):
                return -1
            elif int(new_list_1[i]) > int(new_list_2[i]):
                return 1
        
        return 0
