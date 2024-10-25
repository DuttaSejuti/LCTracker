class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        sorted_folders = sorted(folder, key = len)
        root = TrieNode()
        result = []

        for i in range(len(sorted_folders)):
            folder = sorted_folders[i].split('/')
            flag = 0
            curr = root
            for c in folder:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
                if curr.word:
                    flag = 1
                    break
            if flag == 0:
                curr.word = True
                result.append(sorted_folders[i])

        return result
                   