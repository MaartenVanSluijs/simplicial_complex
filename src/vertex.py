class Vertex:
    '''
        Class that defines a vertex in our complex

        Parameters:
            x (int): x-coordinate of the point
            y (int): y-coordinate of the point
            grid_x (int): The x-coordinate if snapped to a grid
            grid_y (int): The y-coordinate if snapped to a grid
    '''


    def __init__(self, 
                 x: int, 
                 y: int, 
                 grid_x: int | None = None, 
                 grid_y: int | None = None):
        
        self.x = x
        self.y = y
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.drag = False
        
    def move(self, x: int, y: int):
        '''
            Moves the vertex to a new point

            Parameters:
                x (int): The new x-coordinate
                y (int): The new y-coordinate
        '''
        self.x = x
        self.y = y

