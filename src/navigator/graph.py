from src.navigator.base import Navigator


class WeightGraphNavigator(Navigator):
    def __init__(self, width, height) -> None:
        super().__init__(width, height)
    
    def set_graph(self, graph = dict()):
        self.graph = dict(graph)
    
    def set_table_latlon(self, table_latlon = dict()):
        """특정 노드에 대한 위도, 경도 테이블
        """
        self.table_latlon = table_latlon

    def cost_step(self, node, next_node):
        """경로 이동 시, 소요되는 이동 비용
        """
        if self.graph is None:                      raise TypeError
        if node not in self.graph:                  raise KeyError
        if not isinstance(self.graph[node], dict):  raise TypeError
        if next_node not in self.graph[node]:       raise KeyError
        return self.graph[node][next_node]
        
    def heuristic(self, node, target):
        """예상 이동경로 점수. 해당 점수를 기반으로 가장 근접했던 경로를 계산
        """
        (a, b), (x, y) = self.table_latlon[node], self.table_latlon[target]
        # Manhattan 거리
        return ( (x - a)**2 + (y - b)**2 )**0.5 * 1.2

    def step_next(self, node):
        """현재 노드에서 이동가능한 노드
        """
        if self.graph is None:                      raise TypeError
        if node not in self.graph:                  raise KeyError
        if not isinstance(self.graph[node], dict):  raise TypeError
        yield from self.graph[node].keys()
