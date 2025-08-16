import heapq


class Navigator:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def get_path(self, start_node, end_node):
        # (f, g, node, history)
        score, history_min = self.heuristic(start_node, end_node), tuple([start_node])
        queue = [ (score, 0, start_node, history_min) ]
        visited = set()
        while queue:
            f, g, node, history = heapq.heappop(queue)

            # 재방문 금지
            if self.hash(node) in visited: continue
            visited.add(self.hash(node))

            # 노드 유효성 검사
            if not self.validate_node(node): continue

            # 완료 조건
            if node == end_node: return history

            # 스텝 기록
            if f < score:
                score, history_min = f, history

            # 다음 스텝
            for next_node in self.step_next(node):
                g_next = g + self.cost_step(node, next_node)
                f_next = self.heuristic(next_node, end_node) + g_next
                heapq.heappush(queue, (f_next, g_next, next_node, (*history, next_node)))

        return history_min

    def hash(self, node):
        """노드를 식별할 수 있는 해시값. 동일하면 같은 노드로 인식할 수 있음
        """
        return node

    def validate_node(self, node):
        """해당 노드가 존재할 수 있는 노드인지 확인
        """
        return True

    def cost_step(self, node, next_node):
        """경로 이동 시, 소요되는 이동 비용
        """
        return 1
        
    def heuristic(self, node, target):
        """예상 이동경로 점수. 해당 점수를 기반으로 가장 근접했던 경로를 계산
        """
        raise NotImplementedError()

    def step_next(self, node):
        """현재 노드에서 이동가능한 노드
        """
        raise NotImplementedError()
