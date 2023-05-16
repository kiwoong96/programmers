from collections import defaultdict

def solution(tickets):
    path = []
    graph = defaultdict(list)
    
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])

    for airport in graph.keys():
        graph[airport].sort(reverse=True)

    stack = ["ICN"]
    
    while stack:
        top = stack.pop()

        if top not in graph or not graph[top]:
            path.append(top)
        else:
            stack.append(top)
            stack.append(graph[top].pop())

    return path[::-1]

#tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
#print(solution(tickets))