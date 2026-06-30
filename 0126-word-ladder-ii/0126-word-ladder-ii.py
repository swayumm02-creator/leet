from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
            
        parents = defaultdict(list)
        distance = {beginWord: 0}
        queue = deque([beginWord])
        found = False
        
        while queue and not found:
            level_size = len(queue)
            local_visited = set()
            
            for _ in range(level_size):
                word = queue.popleft()
                current_distance = distance[word]
                
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue
                            
                        next_word = word[:i] + c + word[i+1:]
                        
                        if next_word in wordSet:
                            if next_word not in distance:
                                distance[next_word] = current_distance + 1
                                queue.append(next_word)
                                local_visited.add(next_word)
                                parents[next_word].append(word)
                            elif distance[next_word] == current_distance + 1:
                                parents[next_word].append(word)
                                
                            if next_word == endWord:
                                found = True
                                
            wordSet -= local_visited
            
        res = []
        if not found:
            return res
            
        def backtrack(word: str, path: list[str]):
            if word == beginWord:
                res.append([beginWord] + path[::-1])
                return
                
            for parent in parents[word]:
                path.append(word)
                backtrack(parent, path)
                path.pop()
                
        backtrack(endWord, [])
        return res