from vector import Vector2D
from math import radians, sin, cos
import pygame
from pygame.locals import *

def map_to_range(start_val, current_range_min, current_range_max, wanted_range_min, wanted_range_max):
    """Maps x and y from a range to another, desired range"""
    out_range = wanted_range_max - wanted_range_min
    in_range = current_range_max - current_range_min
    in_val = start_val - current_range_min
    val=(float(in_val)/in_range)*out_range
    out_val = wanted_range_min+val
    return out_val

class Camera():
    def __init__(self, x, y, size):
        self.pos = Vector2D(x, y)
        self.FOV = 45
        self.sight_dist = 100
        self.heading = -90
        self.size = int(size)

        self.speed = 5
        self.turn_speed = 5

    def show(self, screen):
        pygame.draw.circle(screen, [100, 150, 100], self.pos.get_xy(int), self.size)

    def show_heading(self, screen):
        for a in range(int(self.heading - self.FOV/2), int(self.heading + self.FOV/2)):
            x = self.sight_dist * cos(radians(a))
            y = self.sight_dist * sin(radians(a))

            x += self.pos.x
            y += self.pos.y

            pygame.draw.line(screen, [0, 200, 0], self.pos.get_xy(int), (int(x), int(y)), 1)

    def draw_ray_cast(self, screen, walls):
        rays = self.ray_cast(walls)

        x = 500
        x_inc = int(500 / self.FOV)
        for point in rays:
            if point is not None:
                pygame.draw.line(screen, [0, 200, 0], self.pos.get_xy(int), point.get_xy(int), 1)

                val = map_to_range(point.data["dist-to-player"], 0, self.sight_dist, 255, 0)
                wall_height = map_to_range(point.data["dist-to-player"], 0, self.sight_dist, 300, 0) + 100

                pygame.draw.rect(screen, [val, val, val], (x, 0, x_inc, wall_height))
                pygame.draw.rect(screen, [51, 51, 51], (x, wall_height - 10, x_inc, screen.get_height() + 10))
            x += x_inc

    def update(self, key):
        if key[K_w] : self.pos.y -= self.speed
        if key[K_a] : self.pos.x -= self.speed
        if key[K_s] : self.pos.y += self.speed
        if key[K_d] : self.pos.x += self.speed

        if key[K_RIGHT] : self.heading += self.turn_speed
        if key[K_LEFT] : self.heading -= self.turn_speed

    def ray_cast(self, walls):
        rays = []
        for a in range(int(self.heading - self.FOV/2), int(self.heading + self.FOV/2), 1):
            x = cos(radians(a))
            y = sin(radians(a))

            ray = Vector2D(x, y)
            heading = Vector2D(x, y)
            heading.normalise()
            ray.add(self.pos)

            farthest = None
            while True:
                if ray.return_rect().collidelist(walls) == -1 and ray.dist(self.pos) <= self.sight_dist:
                    farthest = ray.copy()
                    farthest.data["dist-to-player"] = ray.dist(self.pos)
                    ray.add(heading)
                else:
                    break
            
            rays.append(farthest)

        return rays

















