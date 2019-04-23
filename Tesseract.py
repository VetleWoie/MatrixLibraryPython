import pygame
from Matrix import Matrix
from Matrix import Vector
import math



class Simulation:
    def __init__(self,width, height):
        pygame.init()
        self.size = (width, height)
        self.screen = pygame.display.set_mode(self.size)

        self.project = Matrix(matrix=[  [1,0,0],
                                        [0,1,0] ])

        self.cube = [
                        Matrix(matrix=[[0],[0],[0]]), #1
                        Matrix(matrix=[[1],[0],[0]]), #2
                        Matrix(matrix=[[1],[1],[0]]), #3
                        Matrix(matrix=[[0],[1],[0]]), #4
                        Matrix(matrix=[[0],[0],[1]]), #5
                        Matrix(matrix=[[1],[0],[1]]), #6
                        Matrix(matrix=[[1],[1],[1]]), #7
                        Matrix(matrix=[[0],[1],[1]])  #8
                    ]

        self.simulate()
    
    def simulate(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
        
        
            
Simulation(320,240)





