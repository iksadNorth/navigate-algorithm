import matplotlib.pyplot as plt


class GridPaint:
    def __init__(self) -> None:
        self.fig, self.ax = plt.subplots()
    
    def add_point(self, point, color='black'):
        if not point: return
        
        x, y = point
        self.ax.fill_between([x, x+1], y, y+1, color=color)

    def add_obstacle(self, point):
        self.add_point(point, 'black')

    def add_trace(self, point):
        self.add_point(point, 'gray')

    def generate_gradient(self, start_color, end_color, n):
        """
        start_color, end_color : (R,G,B) 튜플, 0~1 범위
        n : 생성할 색 개수
        return : n개의 RGB 튜플 리스트
        """
        gradient = []
        for i in range(n):
            t = i / (n-1) if n > 1 else 0  # 0~1 비율
            r = start_color[0] + (end_color[0] - start_color[0]) * t
            g = start_color[1] + (end_color[1] - start_color[1]) * t
            b = start_color[2] + (end_color[2] - start_color[2]) * t
            gradient.append((r, g, b))
        return gradient

    def plot_map(self, width, height):

        # 좌표계 맞추기
        self.ax.set_xlim(0, width)
        self.ax.set_ylim(0, height)
        self.ax.set_aspect('equal')

        # 격자 표시
        for x in range(width + 1):
            self.ax.axvline(x, color='lightgray', linewidth=0.5)
        for y in range(height + 1):
            self.ax.axhline(y, color='lightgray', linewidth=0.5)
        
        return self.fig, self.ax
