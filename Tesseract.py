import pygame
from Matrix import Matrix
from Matrix import Vector
import math


RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

SCALE = 50



class Simulation:
    def __init__(self,width, height):
        pygame.init()
        self.size = (width, height)
        self.screen = pygame.display.set_mode(self.size)
        self.scale = SCALE

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
        angle = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            for point in self.cube:
                p = self.project * (point*50)
                p *= self.rotate(3,angle,1,2)
                pygame.draw.circle(self.screen,RED,(p.mat[0][0]+160,p.mat[1][0]+120), 5)
            pygame.display.update()
            angle += 1


    def rotate(self,dim, angle, axis1, axis2):
        axis1 -= 1
        axis2 -= 1

        angle *= 180 / math.pi 
        sine = math.sin(angle)
        cos = math.cos(angle)
        rotation = Matrix(rows=dim, columns=dim)

        rotation.mat[axis1][axis1] = cos
        rotation.mat[axis1][axis2] = -sine
        rotation.mat[axis2][axis1] = sine
        rotation.mat[axis2][axis1] = cos

        return rotation

        
        
            
Simulation(320,240)





