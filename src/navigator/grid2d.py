from src.navigator.base import Navigator


class Grid2dNavigator(Navigator):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def set_obstacles(self, obstacles = set()):
        self.obstacles = set(obstacles)

    def validate_node(self, node):
        """해당 노드가 존재할 수 있는 노드인지 확인
        """
        x, y = node
        if node in self.obstacles:      return False
        if not (0 <= x < self.width):   return False
        if not (0 <= y < self.height):  return False
        return True
        
    def heuristic(self, node, target):
        """예상 이동경로 점수. 해당 점수를 기반으로 가장 근접했던 경로를 계산
        """
        (a, b), (x, y) = node, target
        # Manhattan 거리
        return ( (x - a)**2 + (y - b)**2 )**0.5 * 1.2

    def step_next(self, node):
        """현재 노드에서 이동가능한 노드
        """
        x, y = node
        for dx, dy in [ (-1, 0), (1, 0), (0, -1), (0, 1) ]:
            yield x+dx, y+dy
