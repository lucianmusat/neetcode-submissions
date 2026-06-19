from typing import List
from collections import defaultdict, deque

class Solution:

    def are_close(self, word1: str, word2: str) -> bool:
        diffs = 0
        for letter in range(len(word1)):
            if word1[letter] != word2[letter]:
                diffs += 1
                if diffs > 1:
                    return False
        return True


    # This could be optimized using wildcard templates but let's skip that for now
    # and focus on correctness
    def to_adj_list(self, words: List[str]):
        graph = defaultdict(list)
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if self.are_close(words[i], words[j]):
                        graph[words[i]].append(words[j])
        return graph

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # base cases
        if not beginWord or not endWord:
            return 0

        # Convert words to graph nodes
        nodes = set(wordList)
        nodes.add(beginWord)
        if endWord not in nodes:
            return 0

        # Each node connects to words that are only one letter different
        graph = self.to_adj_list(list(nodes))

        # BFS: word, distance
        q = deque([(beginWord, 1)])
        visited = {beginWord}  # set literal, same as set([word])

        # explore
        while q:
            word, distance = q.popleft()
            if word == endWord:
                return distance

            for close_word in graph[word]:
                if close_word not in visited:
                    visited.add(close_word)
                    q.append((close_word, distance + 1))

        return 0
