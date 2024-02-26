#!/usr/bin/env python3

def search(start: str, final: str, graph: dict, heuristics: dict=None) -> None:
    """
    Performs either uninformed or informed search depending on whether heuristics are provided,
    and prints the search results.
    
    Parameters:
    - start (str): The starting node.
    - final (str): The final/goal node.
    - graph (dict): The graph represented as a dictionary.
    - heuristics (dict, optional): Heuristic values for nodes.
    """
    from queue import PriorityQueue

    track = PriorityQueue()
    track.put((0 if not heuristics else heuristics[start], 0, [start]))
    NP, NG, NE = 0, 1, 0 # accumulators

    visited = set()

    while not track.empty():
        estimated_cost, cost, path = track.get()
        current = path[-1]
        NP += 1 # popped nodes accumulator
        if current == final:
            print(f"Nodes Popped: {NP}")
            print(f"Nodes Expanded: {NE}")
            print(f"Nodes Generated: {NG}")
            print(f"Distance: {cost} km")
            print("Route:")
            for i in range(len(path) - 1):
                print(f"{path[i]} to {path[i+1]}, {graph[path[i]][path[i+1]]} km")
            return
        if current not in visited:
            visited.add(current)
            NE += 1 # expanded nodes accumulator
            for neighbor, distance in graph[current].items():
                new_cost = cost + distance
                NG += 1 # generated nodes accumulator
                estimated_cost = new_cost + heuristics.get(neighbor, float('inf')) if heuristics else new_cost
                track.put((estimated_cost, new_cost, path + [neighbor]))
    print(f"Nodes Popped: {NP}")
    print(f"Nodes Expanded: {NE}")
    print(f"Nodes Generated: {NG}")
    print("Distance: infinity")
    print("Route:\nNone")

if __name__ == "__main__":
    import sys
    from enum import IntEnum, unique

    @unique
    class ExitCode(IntEnum):
        ERROR_ARG_COUNT = 100
        ERROR_GRAPH_FILE = 200
        ERROR_HEURISTIC_FILE = 300

    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print("[USAGE]", "find_route input_filename origin_city destination_city {heuristic_filename}", sep="\n\n")
        sys.exit(ExitCode.ERROR_ARG_COUNT)

    input_file, start, final = sys.argv[1:4]

    # Read graph file
    graph = dict()
    try:
        with open(input_file, 'r') as file:
            for line in file:
                if line.strip() == 'END OF INPUT': break
                start_node, final_node, dist = line.strip().split()
                dist = float(dist)
                graph.setdefault(start_node, dict())[final_node] = dist
                graph.setdefault(final_node, dict())[start_node] = dist
    except Exception as err:
        print("[ERROR reading graph data]", err, file=sys.stderr)
        sys.exit(ExitCode.ERROR_GRAPH_FILE)

    # Read heuristics file (if provided)
    heuristics = None
    if len(sys.argv) == 5:
        heuristic_file = sys.argv[4]
        heuristics = dict()
        try:
            with open(heuristic_file, 'r') as file:
                for line in file:
                    if line.strip() == 'END OF INPUT': break
                    node, value = line.strip().split()
                    heuristics[node] = float(value)
        except Exception as err:
            print("[ERROR reading heuristics file]", err, file=sys.stderr)
            sys.exit(ExitCode.ERROR_HEURISTIC_FILE)

    search(start, final, graph, heuristics)
