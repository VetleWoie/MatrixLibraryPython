import pygame
from Matrix import Matrix
from Matrix import Vector
import math


RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

SCALE = 200
DOTSIZE = 2
WIDTH = 2



class Simulation:
    def __init__(self,width, height,dim):
        pygame.init()
        self.size = (width, height)
        self.screen = pygame.display.set_mode(self.size)
        self.scale = SCALE
        self.dim = dim
        self.clock = pygame.time.Clock()

        self.projection = self.project(dim,2)
        self.project(dim,dim-1)
        self.cube = self.box(dim)

        self.simulate()

    def project(self,fromDim, toDim):

        projection = Matrix(rows=toDim,columns=fromDim)
        for i in range(toDim):
            projection.mat[i][i] = 1
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
        draw = False
        angle = 0
        lines = False
        while True:
            points = []
            if not draw:
                self.screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        draw = not draw
                    elif event.key == pygame.K_l:
                        lines = not lines
            for point in self.cube:
                for i in range(self.dim-1):
                    point = self.rotate(self.dim,angle,i,i+1) * point
                point = point * self.scale
                point = self.projection * point 
                point.mat[0][0] = int(point.mat[0][0] + self.size[0]/2)
                point.mat[1][0] = int(point.mat[1][0] + self.size[1]/2)
                points.append(point)

            if lines:
                self.lines(points,RED)
            for i in points:
                pygame.draw.circle(self.screen,RED,(i.mat[0][0],i.mat[1][0]),DOTSIZE)
            
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

        for i in range(dim):
            if not(i == axis1 or i == axis2):
                rotation.mat[i][i] = 1 
        return rotation

    def lines(self,points,color):
        for i in range(0,len(points),4):
            p1 = (points[i].mat[0][0] ,  points[i].mat[1][0])
            p2 = (points[i+1].mat[0][0] ,  points[i+1].mat[1][0])
            p3 = (points[i+2].mat[0][0] , points[i+2].mat[1][0])
            p4 = (points[i+3].mat[0][0] , points[i+3].mat[1][0])
            pygame.draw.line(self.screen,color,p1,p2,WIDTH)
            pygame.draw.line(self.screen,color,p1,p3,WIDTH)
            pygame.draw.line(self.screen,color,p2,p4,WIDTH)
            pygame.draw.line(self.screen,color,p3,p4,WIDTH)

        for j in range(3,self.dim+1):
            for i in range(int(len(points)/2)):
                p1 = (points[i].mat[0][0] ,  points[i].mat[1][0])
                p2 = (points[i+(2**(j-1))].mat[0][0] ,  points[i+(2**(j-1))].mat[1][0])
                pygame.draw.line(self.screen,color,p1,p2,WIDTH)
            

            
        
            
Simulation(500,500,3)





