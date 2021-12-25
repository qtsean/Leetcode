class Solution:
    def shortestPathLength(self, graph):
        queue = []
        used = set()
        total = 0
        for i in range(len(graph)):
            queue.append([i, 1 << i])
            used.add((i, 1 << i))
            total += 1 << i
        step = 0
        while queue:
            tmp = []
            for q in queue:
                node, mask = q
                if mask == total:
                    return step
                for neighbor in graph[node]:
                    new_mask = mask | 1 << neighbor
                    if (neighbor, new_mask) not in used:
                        used.add((neighbor, new_mask))
                        tmp.append([neighbor, new_mask])
            queue = tmp
            step += 1