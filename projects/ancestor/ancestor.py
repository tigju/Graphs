"""
diagram

10
/
1  2   4  11
\ /   / \ /
 3   5   8
  \ / \   \
   6   7   9
"""
"""
Example input
  6

1 3
2 3
3 6
5 6
5 7
4 5
4 8
8 9
11 8
10 1

Example output
  10
"""
"""
Adjecency list looks like this:
{
    3: {1, 2}, 
    6: {3, 5}, 
    7: {5}, 
    5: {4}, 
    8: {11, 4}, 
    9: {8}, 
    1: {10}
}
"""

from collections import deque

# solution without graph building
# def earliest_ancestor(ancestors, starting_node):
    
#     stack = deque()
#     visited = set()

#     stack.append(starting_node)

#     while len(stack) > 0:
#         curr_node = stack.pop()
    
#         if curr_node not in visited:
#             visited.add(curr_node)

#             for ancestor in ancestors:
#                 if curr_node == ancestor[1]:
#                     stack.append(ancestor[0])
    
#     if curr_node == starting_node:
#         curr_node = -1
                
#     return curr_node

# solution with the graph building
def earliest_ancestor(ancestors, starting_node):
    ancestors_dict = {}
    for ancestor in ancestors:
        if ancestor[1] in ancestors_dict:
            ancestors_dict[ancestor[1]].add(ancestor[0])
        else:
            ancestors_dict[ancestor[1]] = set()
            ancestors_dict[ancestor[1]].add(ancestor[0])
    
    stack = deque()
    visited = set()

    stack.append(starting_node)

    while len(stack) > 0:
        curr_node = stack.pop()

        if curr_node not in visited:
            visited.add(curr_node)

            for anc in ancestors_dict:

                if curr_node == anc:
                    curr_node = min(ancestors_dict[anc])
                    stack.append(curr_node)
    if curr_node == starting_node:
        curr_node = -1
    return curr_node

pairs = [(1,3), (2,3), (3,6), (5,6), (5,7), (4,5), (4,8), (8,9), (11,8), (10,1)]

print(earliest_ancestor(pairs, 1))
print(earliest_ancestor(pairs, 2))
print(earliest_ancestor(pairs, 3))
print(earliest_ancestor(pairs, 4))
print(earliest_ancestor(pairs, 5))
print(earliest_ancestor(pairs, 6))
print(earliest_ancestor(pairs, 7))
print(earliest_ancestor(pairs, 8))
print(earliest_ancestor(pairs, 9))
print(earliest_ancestor(pairs, 10))
print(earliest_ancestor(pairs, 11))
