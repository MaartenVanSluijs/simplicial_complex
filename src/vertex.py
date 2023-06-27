class Vertex:
    def __init__(self, 
                 x: int, 
                 y: int, 
                 grid_x: int | None = None, 
                 grid_y: int | None = None):
        
        self.x = x
        self.y = y
        self.grid_x = grid_x
        self.grid_y = grid_y
        
    def move(self, x: int, y, int):
        self.x = x
        self.y = y

