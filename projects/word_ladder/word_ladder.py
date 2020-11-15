"""
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
Note:

Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.

Sample:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
["hit", "hot", "dot", "dog", "cog"]

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
[]

1. Translate the problem into graph terminology
vertex - a word
edge - possible one letter transformation from a word
to another word (undirected)
path - transformations of a word
weights - n/a

2. Build your graph
- we can create all possible transformations of
beginWord and its transformations, but that would
waste a lot of memory

- we can come up with how to find out
the next vertex by determining if it's
a valid vertex to visit

- instead, we can determine which vertex
to visit next if the transformation is in the wordList

3. Traverse the graph
- shortest = BFS
- we can traverse the graph using BFS and a queue
- use a set to avoid re-visiting nodes
- start from beginWord, and generate word transformations from it.
enqueue nodes that are in the wordList
- keep track of the path we're currently on as we're traversing via
a list
- once we find endWord, then we simply return the path
to that node
"""

from collections import deque

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def get_neighbors(word, wordList):
    wordSet = set(wordList)
    neighbors = set()
    stringWord = list(word)
    for i in range(len(stringWord)):
        for letter in alphabet:
            newWord = list(stringWord)
            newWord[i] = letter
            newWordString = "".join(newWord)

            if newWordString in wordSet and newWordString != word:
                neighbors.add(newWordString)
    return neighbors

def findLadders(beginWord, endWord, wordList):
    queue = deque()
    visited = set()
    queue.append([beginWord])
    while len(queue) > 0:
        currPath = queue.popleft()
        currWord = currPath[-1]
        if currWord not in visited:
            if currWord == endWord:
                return currPath

            visited.add(currWord)
            for neighbor_word in get_neighbors(currWord, wordList):
                newPath = list(currPath)
                newPath.append(neighbor_word)
                queue.append(newPath)
    return []

# no helper function


# def findLadders(beginWord, endWord, wordList):
#     words = set(wordList)
#     visited = set()
#     queue = deque()
#     queue.append([beginWord])
#     while len(queue) > 0:
#         currPath = queue.popleft()
#         currWord = currPath[-1]
#         if currWord in visited:
#             continue
#         visited.add(currWord)
#         if currWord == endWord:
#             return currPath
#         for i in range(len(currWord)):
#             for letter in alphabet:
#                 transformedWord = currWord[:i] + letter + currWord[i + 1:]
#                 if transformedWord in words:
#                     newPath = list(currPath)
#                     newPath.append(transformedWord)
#                     queue.append(newPath)
#     return []

"""
['hit', 'hot', 'dot', 'dog', 'cog']
"""
a = findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
print(a)

"""
empty []
"""

b = findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
print(b)
