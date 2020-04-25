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

        self.cruise_res = 1
        self.high_qual_res = 0.1
        self.res = self.cruise_res
        self.key_counter = 5

    def show(self, screen, walls):
        pygame.draw.circle(screen, [100, 150, 100], self.pos.get_xy(int), self.size)
        self.draw_ray_cast(screen, walls)

    def draw_ray_cast(self, screen, walls):
        screen_w, screen_h = screen.get_size()
        screen_w /= 2

        a = self.heading - (self.FOV/2)
        a_inc = self.res

        x_inc = screen_w / (self.FOV / a_inc)
        wall_x = 500
        while a < self.heading + (self.FOV/2):
            # turn the heading
            x = cos(radians(a))
            y = sin(radians(a))
            a += a_inc

            # create heading
            heading = Vector2D(x, y)
            heading.normalise()

            # create and start raycast
            ray = self.pos.copy()
            while True:
                # step the ray
                ray.add(heading)
                # check if the ray is out of the render distance, render distance has a buffer to account for overruns
                if ray.dist(self.pos, use_sqrt=False) >= (self.sight_dist**2) - 5 : break
                # check if the ray has collided
                if ray.return_rect().collidelist(walls) != -1 : break

            # work out distance to player
            dist_to_player = int(ray.dist(self.pos, use_sqrt=False))

            # create wall colour based on the dist
            color = map_to_range(dist_to_player, 0, self.sight_dist**2, 255, 0)
            color = [color for _ in range(3)]

            # create wall size based on the dist
            wall_h = map_to_range(dist_to_player, 0, self.sight_dist**2, screen_h, 0)

            buffer = 100
            # draw wall
            if wall_h != 0:
                wall_y = wall_h/4
                wall_w = x_inc + (x_inc * int(self.res == self.high_qual_res))
                wall_h = (wall_h / 2) + buffer
                pygame.draw.rect(screen, color, (int(wall_x), wall_y, int(wall_w), int(wall_h)))

            wall_x += x_inc

            # draw ray
            # pygame.draw.line(screen, [0, 200, 0], self.pos.get_xy(int), ray.get_xy(int), 1)

            # draw heading
            x = (self.sight_dist * cos(radians(self.heading))) + self.pos.x
            y = (self.sight_dist * sin(radians(self.heading))) + self.pos.y
            pygame.draw.line(screen, [0, 200, 0], self.pos.get_xy(int), (int(x), int(y)), 1)

    def get_forward(self):
        x = cos(radians(self.heading))
        y = sin(radians(self.heading))
        vec = Vector2D(x, y)
        vec.normalise()

        return vec

    def get_right(self):
        x = cos(radians(self.heading + 90))
        y = sin(radians(self.heading + 90))
        vec = Vector2D(x, y)
        vec.normalise()

        return vec

    def update(self, key):
        vel = Vector2D()


        if key[K_w]:
            heading = self.get_forward()
            heading.mult(self.speed)
            vel.add(heading)
        if key[K_a]:
            heading = self.get_right()
            heading.mult(-self.speed)
            vel.add(heading)
        if key[K_s]:
            heading = self.get_forward()
            heading.mult(-self.speed)
            vel.add(heading)
        if key[K_d]:
            heading = self.get_right()
            heading.mult(self.speed)
            vel.add(heading)

        self.pos.add(vel)

        if key[K_RIGHT] : self.heading += self.turn_speed
        if key[K_LEFT] : self.heading -= self.turn_speed

        if key[K_DOWN] and self.key_counter <= 0: self.res = self.cruise_res ; self.key_counter = 5
        if key[K_UP] and self.key_counter <= 0: self.res = self.high_qual_res ; self.key_counter = 5
        self.key_counter -= 1

















