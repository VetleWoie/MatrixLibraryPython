import pygame
from Matrix import Matrix
from Matrix import Vector
import math


RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

SCALE = 100



class Simulation:
    def __init__(self,width, height,dim):
        pygame.init()
        self.size = (width, height)
        self.screen = pygame.display.set_mode(self.size)
        self.scale = SCALE
        self.dim = dim
        self.clock = pygame.time.Clock()

        self.projection = self.project(dim)
        self.cube = self.box(dim)

        self.simulate()

    def project(self,dim):

        projection = Matrix(rows=2,columns=dim)
        projection.mat[0][0] = 1
        projection.mat[1][1] = 1
        return projection
    
    def box(self,dim):
        corners = 2**dim
        cube = []
        for i in range(corners):
            cube.append(Matrix(rows=dim,columns=1))
            for j in range(dim):
                cube[i].mat[j][0] = -0.5

        for i in range(corners):
            for k,j in zip(range(dim),reversed(bin(i))):
                if j == '1':
                    cube[i].mat[k][0] *= -1
                elif j == 'b':
                    break
                else:
                    continue
        return cube



    def simulate(self):
        angle = 0
        while True:
            self.screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            for point in self.cube:
                point = self.rotate(self.dim,angle,1,2) * point
                point = point * self.scale
                point = self.projection * point
                
                pygame.draw.circle(self.screen,RED,(int(point.mat[0][0] + self.size[0]/2),int(point.mat[1][0]+self.size[1]/2)), 5)
            pygame.display.update()

            angle += 0.001
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

        for i in range(dim):
            if i != axis1 or i != axis2:
                rotation.mat[i][i] = 1 
        return rotation
       
        
            
Simulation(500,500,3)





