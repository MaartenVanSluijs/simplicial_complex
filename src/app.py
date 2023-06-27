from src.vertex import Vertex

import pygame
import sys


class App():

    '''
        The app
    '''

    def __init__(self):

        self.SIZE = WIDTH, HEIGHT = 1000, 620
        self.SCREEN = pygame.display.set_mode(self.SIZE)
        self.FRAME_RATE = 60
        self.RADIUS = 10
        
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)

        pygame.init()

        self.clock = pygame.time.Clock()

        pygame.display.set_caption('Simplicial Complex Drawing Tool')

        self.vertices: list[Vertex] = []

    def run(self):
        '''
            Contains the main loop, routes actions, and updates the screen
        '''

        while True:

            self.clock.tick(self.FRAME_RATE)

            # Handle events
            for event in pygame.event.get():

                # Allow user to close the window without crashing
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mousepress(event)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.handle_mouserelease()
                elif event.type == pygame.MOUSEMOTION:
                    self.handle_movement(event)


            self.render_screen()
            pygame.display.flip()

    def handle_movement(self, event: pygame.event):
        '''
            Handles mouse movement, drags points across the screen when they are selected

            Parameters:
                event (pygame.event): The event that triggered this function
        '''
        position = event.pos
        for vertex in self.vertices:
            if vertex.drag:
                vertex.move(position[0], position[1])

    def handle_mouserelease(self):
        '''
            Handles mouse releases, stops dragging all points
        '''
        for vertex in self.vertices:
            vertex.drag = False

    def handle_mousepress(self, event: pygame.event):
        '''
            Handles mousepresses.

                Parameters: 
                    event (pygame.event): the mouse_pressed event
        '''

        # The position of the event
        position = event.pos

        # For checking if a point is clicked
        on_point = False

        # If the left mouse button is pressed
        if pygame.mouse.get_pressed()[0]:

            # Check if a point or an empty space is pressed
            for vertex in self.vertices:
                if self.compute_distance((vertex.x, vertex.y), position) < self.RADIUS:
                    on_point = True
                    vertex.drag = True

            # If a point is not selected
            if not on_point:
                vertex = Vertex(position[0], position[1])
                self.vertices.append(vertex)

        # if the right mouse button is pressed
        elif pygame.mouse.get_pressed()[2]:
            for vertex in self.vertices:
                distance = self.compute_distance((vertex.x, vertex.y), position)
                if distance < self.RADIUS:
                    self.vertices.remove(vertex)
        
    def render_screen(self):
        '''
            Renders the app elements on the screen
        '''

        self.SCREEN.fill(self.WHITE)
        for vertex in self.vertices:
            pygame.draw.circle(self.SCREEN, self.BLACK, (vertex.x, vertex.y), self.RADIUS)

    def compute_distance(self, first_point: tuple[int], second_point: tuple[int]) -> float:
        '''
            Computes the euclidian distance between two points

            Parameters:
                first_point (tuple(int)): The coordinates of the first point
                second_point (tuple(int)): The coordinates of the second point
        '''
        diff = (first_point[0] - second_point[0], first_point[1] - second_point[1])
        distance = (diff[0]**2 + diff[1]**2) ** 0.5
        return distance
        