from random import randrange


class EnvSetter:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def filter_obstacles(self, black_list: set = set()):
        return {
            (black_x, black_y) 
            for black_x, black_y in black_list 
            if ( 0 <= black_x < self.width) and ( 0 <= black_y < self.height)
        }
    
    def get_obstacles(self, black_list: set = set()):
        if not isinstance(black_list, set):
            black_list = set(black_list)
        
        black_list = self.filter_obstacles(black_list)
        
        limit = self.width * self.height- len(black_list)
        if limit <= 0: return
        
        result = set()
        for _ in range(100000000):
            if limit <= len(result): break
            obst_point = (randrange(0, self.width), randrange(0, self.height))
            
            if obst_point in black_list: continue
            if obst_point in result: continue
            
            yield obst_point
            result.add(obst_point)
