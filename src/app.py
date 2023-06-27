from src.vertex import Vertex

import pygame
import sys


class App():

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

        while True:

            self.clock.tick(self.FRAME_RATE)

            # Handle events
            for event in pygame.event.get():

                # Allow user to close the window without crashing
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mousepress(event)


            self.render_screen()
            pygame.display.flip()

    def handle_mousepress(self, event: pygame.event):
        position = event.pos


        if pygame.mouse.get_pressed()[0]:
            vertex = Vertex(position[0], position[1])
            self.vertices.append(vertex)
        elif pygame.mouse.get_pressed()[2]:
            for vertex in self.vertices:
                diff = (vertex.x - position[0], vertex.y - position[1])
                distance = (diff[0]**2 + diff[1]**2) ** 0.5
                if distance < self.RADIUS:
                    self.vertices.remove(vertex)
        
    def render_screen(self):
        self.SCREEN.fill(self.WHITE)
        for vertex in self.vertices:
            pygame.draw.circle(self.SCREEN, self.BLACK, (vertex.x, vertex.y), self.RADIUS)