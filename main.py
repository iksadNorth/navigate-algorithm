import matplotlib.pyplot as plt
from itertools import islice
from src.plot_handler import GridPaint
from src.navigator import Navigator
from src.env_setter import EnvSetter


def main():
    width, height, num_obst = 100, 100, 2000
    start, goal = (0,0), (width-1, height-1)
    start_color, end_color = (0.2,0.7,0.1), (1,0,0)

    env_setter = EnvSetter(width, height)
    navigator = Navigator(width, height)

    # 장애물 정의
    obstacles = env_setter.get_obstacles(black_list={start, goal})
    obstacles = islice(obstacles, num_obst)
    obstacles = list(obstacles)
    navigator.set_obstacles(obstacles)

    # 경로 계산
    traces = navigator.get_path(start, goal)
    
    # 그래프 그리기
    grid_paint = GridPaint()
    grid_paint.plot_map(width, height)
    for obstacle in obstacles:
        grid_paint.add_obstacle(obstacle)
    color_map = grid_paint.generate_gradient(start_color, end_color, len(traces))
    for trace, color in zip(traces, color_map):
        grid_paint.add_point(trace, color)
    plt.show()


if __name__ == "__main__":
    main()
