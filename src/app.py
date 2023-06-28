from src.vertex import Vertex

import sys
import pygame
import pygame_widgets as widgets
from pygame_widgets.toggle import Toggle
from pygame_widgets.button import Button

class App():

    '''
        The app
    '''

    def __init__(self):

        self.SIZE = self.WIDTH, self.HEIGHT = 1000, 700
        self.SCREEN = pygame.display.set_mode(self.SIZE)
        self.INFO_SIZE = 80
        self.FRAME_RATE = 60
        self.RADIUS = 10
        
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.GRAY = (150,150,150)

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


            self.render_screen(pygame.event.get())
            pygame.display.flip()

    def handle_movement(self, event: pygame.event):

        '''
            Handles mouse movement, drags points across the screen when they are selected

            Parameters:
                event (pygame.event): The event that triggered this function
        '''
        
        position = event.pos
        # Loop through all vertices
        for vertex in self.vertices:
            # If the to be dragged vertices are found
            if vertex.drag:
                # If the mouse is inside the canvas
                if position[1] > self.INFO_SIZE:
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
                # If the click was on the canvas
                if position[1] > self.INFO_SIZE:
                    vertex = Vertex(position[0], position[1])
                    self.vertices.append(vertex)

        # if the right mouse button is pressed
        elif pygame.mouse.get_pressed()[2]:
            for vertex in self.vertices:
                distance = self.compute_distance((vertex.x, vertex.y), position)
                if distance < self.RADIUS:
                    self.vertices.remove(vertex)
        
    def render_screen(self, events):
        
        '''
            Renders the app elements on the screen
        '''

        # Fill the screen with white
        self.SCREEN.fill(self.WHITE)

        self.draw_menu()

        # Draw all the vertices
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
        
    def draw_menu(self):
        # Draw the menu box on the top
        menu_rectangle = pygame.Rect(0, 0, self.WIDTH, self.INFO_SIZE)
        pygame.draw.rect(self.SCREEN, self.GRAY, menu_rectangle)
        pygame.draw.line(self.SCREEN, self.BLACK, (0, self.INFO_SIZE), (self.WIDTH, self.INFO_SIZE), 3)