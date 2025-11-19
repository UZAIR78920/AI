tree = {
    1: [2, 9, 10],
    2: [3, 4],
    3: [],
    4: [5, 6, 7],
    5: [8],
    6: [],
    7: [],
    8: [],
    9: [],
    10: []
}

def breadth_first_search(tree, start):
    q = [start]
    visited = []
    while q:
        print("before", q)
        node = q.pop(0)
        visited.append(node)
        for child in (tree[node]):
            if child not in visited and child not in q:
                q.append(child)
        print("after", q)
    return visited

result = breadth_first_search(tree, 1)
print(result)

# Output:
# before [1]
# after [2, 9, 10]
# before [2, 9, 10]
# after [9, 10, 3, 4]
# before [9, 10, 3, 4]
# after [10, 3, 4]
# before [10, 3, 4]
# after [3, 4]
# before [3, 4]
# after [4]
# before [4]
# after [5, 6, 7]
# before [5, 6, 7]
# after [6, 7, 8]
# before [6, 7, 8]
# after [7, 8]
# before [7, 8]
# after [8]
# before [8]
# after []
# [1, 2, 9, 10, 3, 4, 5, 6, 7, 8]
