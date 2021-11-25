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


def breadth_first_graph_search_shortest_path(original_graph: dict, el_from: str, el_to: str):
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
        optimal_path = breadth_first_graph_search_shortest_path(graph, from_, to)
        print(f'Optimal path is {optimal_path}')

"""
Imagine that someone named Tom has guitar and want to trade it
with his friends. He will pay them for successful trade
and get different things from each one.
Tom going to receive minimum lesion and piano.
"""

graph = dict()
graph['guitar'] = {}  # Tom has 3 friends with different things and surcharges
