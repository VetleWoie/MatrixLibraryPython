import pygame
from Matrix import Matrix
from Matrix import Vector
import math


RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

SCALE = 50



class Simulation:
    def __init__(self,width, height):
        pygame.init()
        self.size = (width, height)
        self.screen = pygame.display.set_mode(self.size)
        self.scale = SCALE
        self.clock = pygame.time.Clock()

        self.project = Matrix(matrix=[  [1,0,0,0],
                                        [0,1,0,0],
                                     ])

        self.cube = [
                        Matrix(matrix=[[0.5],[0.5],[-0.5],[-0.5]]), #1
                        Matrix(matrix=[[-0.5],[0.5],[-0.5],[-0.5]]), #2
                        Matrix(matrix=[[-0.5],[-0.5],[-0.5],[-0.5]]), #3
                        Matrix(matrix=[[0.5],[-0.5],[-0.5],[-0.5]]), #4
                        Matrix(matrix=[[0.5],[0.5],[0.5],[-0,5]]), #5
                        Matrix(matrix=[[-0.5],[0.5],[0.5],[-0.5]]), #6
                        Matrix(matrix=[[-0.5],[-0.5],[0.5],[-0.5]]), #7
                        Matrix(matrix=[[0.5],[-0.5],[0.5],[-0.5]]),  #8
                        Matrix(matrix=[[0.5],[0.5],[-0.5],[0.5]]), #1
                        Matrix(matrix=[[-0.5],[0.5],[-0.5],[0.5]]), #2
                        Matrix(matrix=[[-0.5],[-0.5],[-0.5],[0.5]]), #3
                        Matrix(matrix=[[0.5],[-0.5],[-0.5],[0.5]]), #4
                        Matrix(matrix=[[0.5],[0.5],[0.5],[0,5]]), #5
                        Matrix(matrix=[[-0.5],[0.5],[0.5],[0.5]]), #6
                        Matrix(matrix=[[-0.5],[-0.5],[0.5],[0.5]]), #7
                        Matrix(matrix=[[0.5],[-0.5],[0.5],[0.5]])  #8
                    ]

        self.simulate()
    
    def box(self,dim):
        pass

    def simulate(self):
        angle = 0
        while True:
            #self.screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            for point in self.cube:
                point = self.rotateZ(angle) * point
                point = self.rotateY(angle) * point
                point = self.rotateX(angle) * point
                point = self.rotateW(angle) * point
                point = point * 500
                point = self.project * point
                
                pygame.draw.circle(self.screen,RED,(int(point.mat[0][0] + self.size[0]/2),int(point.mat[1][0]+self.size[1]/2)), 5)
            pygame.display.update()

            angle += 0.0001
            self.clock.tick(60)


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
        rotation.mat[axis2][axis2] = cos

        return rotation
    
    def rotateZ(self,angle):
        angle *= 180 / math.pi 
        sine = math.sin(angle)
        cos = math.cos(angle)

        return Matrix(matrix=[[cos,-sine,0,0],[sine,cos,0,0],[0,0,1,0],[0,0,0,0]])

    def rotateY(self,angle):
        angle *= 180 / math.pi 
        sine = math.sin(angle)
        cos = math.cos(angle)

        return Matrix(matrix=[[cos,0,-sine,0],[0,1,0,0],[sine,0,cos,0],[0,0,0,0]])

    def rotateX(self,angle):
        angle *= 180 / math.pi 
        sine = math.sin(angle)
        cos = math.cos(angle)

        return Matrix(matrix=[[1,0,0,0],[0,cos,-sine,0],[0,sine,cos,0],[0,0,0,0]])
    
    def rotateW(self,angle):
        angle *= 180 / math.pi 
        sine = math.sin(angle)
        cos = math.cos(angle)

        return Matrix(matrix=[[1,0,0,0],[0,0,cos,-sine],[0,0,0,0],[0,0,cos,sine]])
       
        
            
Simulation(1000,1000)





