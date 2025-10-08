class Node:
    def __init__(self, name, heuristic=0):
        self.name = name
        self.heuristic = heuristic
        self.solved = False
        self.children = []

    def add_child(self, child_type, child_nodes, cost):
        self.children.append((child_type, child_nodes, cost))

def AO_star(node):
    print(f"\nExpanding node: {node.name}")
    if node.solved:
        return node.heuristic
    if not node.children:
        node.solved = True
        return node.heuristic
    best_cost = float('inf')
    best_choice = None
    for child_type, child_nodes, cost in node.children:
        total_cost = cost
        if child_type == 'AND':
            for child in child_nodes:
                total_cost += child.heuristic
        elif child_type == 'OR':
            total_cost += child_nodes[0].heuristic
        if total_cost < best_cost:
            best_cost = total_cost
            best_choice = (child_type, child_nodes, cost)
    print(f"Best path from {node.name} → {[c.name for c in best_choice[1]]} (type: {best_choice[0]}) with cost: {best_cost}")
    node.heuristic = best_cost
    if best_choice[0] == 'AND':
        for child in best_choice[1]:
            AO_star(child)
        if all(child.solved for child in best_choice[1]):
            node.solved = True
    else:
        AO_star(best_choice[1][0])
        if best_choice[1][0].solved:
            node.solved = True
    return node.heuristic

A = Node('A')
B = Node('B')
C = Node('C', heuristic=0)
D = Node('D')
E = Node('E', heuristic=3)
G = Node('G', heuristic=0)
H = Node('H', heuristic=0)

D.add_child('OR', [G], 0)
D.add_child('OR', [H], 0)
B.add_child('AND', [D, E], 0)
A.add_child('OR', [B], 0)
A.add_child('OR', [C], 0)

print("AO* SEARCH OUTPUT:")
final_cost = AO_star(A)
print(f"\nFinal solution cost for node {A.name}: {final_cost}")