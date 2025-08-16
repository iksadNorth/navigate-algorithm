from networkx import MultiDiGraph
import osmnx as ox

import pickle
from pathlib import Path
from collections import defaultdict


def get_multi_di_graph(cache_file):
    if not Path(cache_file).exists():
        G = ox.graph_from_place("Seoul, South Korea", network_type="drive")
        ox.save_graphml(G, cache_file)
    return ox.load_graphml(cache_file)

def get_cache(filename, callback):
    if not Path(filename).exists():
        with open(filename, "wb") as f:
            object = callback()
            pickle.dump(object, f)
    with open(filename, "rb") as f:
        result = pickle.load(f)
    return result

def get_graph(multi_di_graph: MultiDiGraph):
    graph_dict = {}
    for u, v, data in multi_di_graph.edges(data=True):
        graph_dict = defaultdict(dict)
        graph_dict[u][v] = data  # 도로 정보(거리, 속도 제한 등)
    return graph_dict

def main():
    def get_graph_seoul():
        G: MultiDiGraph = get_multi_di_graph("cache/seoul_drive.graphml")
        return get_graph(G)
    graph_dict = get_cache("cache/seoul_drive.pkl", get_graph_seoul)

    print(list(graph_dict.items())[:3])  # 일부만 출력


if __name__ == "__main__":
    main()
