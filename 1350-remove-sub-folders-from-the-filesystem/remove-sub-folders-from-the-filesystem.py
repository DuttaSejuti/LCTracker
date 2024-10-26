class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_folder = False
    
    def insert(self, path: str) -> bool:
        curr = self
        # as the string starts with /, this will create an empty string for the first /, hence string[1:]
        folder = path[1:].split('/')
        for c in folder:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            if curr.end_of_folder:
                return False
        curr.end_of_folder = True
        return True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = TrieNode()
        sorted_folders = sorted(folder, key = len)
        result = []

        for i in range(len(sorted_folders)):
            folder = sorted_folders[i]
            insert_possible = trie.insert(folder) 
            if insert_possible:
                result.append(folder)
        return result
