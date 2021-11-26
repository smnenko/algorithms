from collections import deque

"""
Simple objective that represents a shortest way from Vitebsk to Warsaw
using graph.
"""

graph = {
    'Vitebsk': ['Minsk', 'Moscow', 'Saint Petersburg'],
    'Minsk': ['Moscow', 'Saint Petersburg', 'Grodno'],
    'Moscow': ['Saint Petersburg', 'Los Angeles', 'Orsha'],
    'Saint Petersburg': ['Moscow', 'Brest', 'Gomel'],
    'Grodno': ['Warsaw'],
    'Los Angeles': ['Ivanovo'],
    'Brest': ['Vitebsk'],
    'Ivanovo': ['Warsaw']
}


def breadth_first_graph_search(original_graph: dict, el_from: str, el_to: str):
    queue = deque()
    queue += original_graph[el_from]
    visited_location = {el_from}
    while queue:
        current = queue.popleft()
        if current == el_to:
            return True
        elif original_graph.get(current):
            for to_visit in original_graph.get(current):
                if to_visit not in visited_location:
                    visited_location.add(to_visit)
                    queue += original_graph[current]
    return False


def breadth_first_graph_search_shortest_path(
        original_graph: dict,
        el_from: str,
        el_to: str
):
    queue = deque()
    queue += [[i] for i in original_graph[el_from]]
    visited_location = [el_from]
    while queue:
        current = queue.popleft()
        node = current[-1]

        if node not in visited_location:
            neighbours = original_graph[node]
            for neighbour in neighbours:
                new_path = list(current)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == el_to and [neighbour] in queue:
                    return [neighbour]
                elif neighbour == el_to:
                    return new_path
            visited_location.append(current)
    return False


if __name__ == '__main__':
    from_ = 'Vitebsk'
    to = 'Warsaw'
    is_optimal_path = breadth_first_graph_search(graph, from_, to)
    print(f'Optimal path was {"found" if is_optimal_path else "not found"}')
    if is_optimal_path:
        path = breadth_first_graph_search_shortest_path(graph, from_, to)
        print(f'Optimal path is {" -> ".join(path)}')


graph = dict()
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['end'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5
graph['end'] = {}

infinity = float('inf')
costs = {'a': 6, 'b': 2, 'end': infinity}

parents = {'a': 'start', 'b': 'start', 'end': None}

processed = []


def find_lowest_cost_node(costs_):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs_:
        cost = costs_[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def djikstra_algorithm(graph_, costs_, parents_):
    node = find_lowest_cost_node(costs_)
    while node is not None:
        cost = costs_[node]
        neighbors = graph_[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs_[n] > new_cost:
                costs_[n] = new_cost
                parents_[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs_)
    return costs_


if __name__ == '__main__':
    to = 'end'
    recalculated_costs = djikstra_algorithm(graph, costs, parents)
    print(f'\nYou can go to {to.upper()} by {recalculated_costs[to]}')
