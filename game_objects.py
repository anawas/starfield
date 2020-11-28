import random
import pygame
from perlin_noise import PerlinNoise

class Star:
    def __init__(self, screen):
        self.screen = screen
        self.scr_width = screen.get_size()[0]
        self.scr_height = screen.get_size()[1]
        self.radius = 1
        self.velocity = 8
        self.x = random.randint(0, self.scr_width)
        self.y = random.randint(0, self.scr_height)
        self.z = random.randint(1, 10)
        self.color = self._set_color()

    def _set_color(self):
        gray_value = 255-self.z
        if gray_value <= 0:
            gray_value = 0

        red = gray_value
        green = gray_value
        blue = gray_value
        return (red, green, blue)

    def update(self):
        if self.done():
            return
        pygame.draw.circle(self.screen, self._set_color(), self.translate(), self.radius)



class RadialStar(Star):
    def __init__(self, screen):
        super().__init__(screen)
        self.x = random.randint(-self.scr_width/2, self.scr_width/2)
        self.y = random.randint(-self.scr_height/2, self.scr_height/2)
        self.z = random.randint(100, 500)

    def translate(self):        
        self.z -= self.velocity
        scr_x = 200*self.x/self.z + self.scr_width / 2
        scr_y = 200*self.y/self.z + self.scr_height / 2
        return (scr_x, scr_y)
    
    def done(self):
        if self.z <= self.velocity:
            return True
        return False
        

class HorizontalStar:
    def __init__(self, screen):
        self.screen = screen
        self.scr_width = screen.get_size()[0]
        self.scr_height = screen.get_size()[1]
        self.radius = 1
        self.x = random.randint(0, self.scr_width)
        self.y = random.randint(0, self.scr_height)
        self.z = random.randint(1, 10)
        self.color = self.__set_color()

    def __set_color(self):
        gray_value = 20*self.z
        if gray_value <= 0:
            gray_value = 0

        red = gray_value
        green = gray_value
        blue = gray_value
        return (red, green, blue)

    def update(self):
        if self.done():
            return
        pygame.draw.circle(self.screen, self.__set_color(), self.translate(), self.radius)

    def translate(self):        
        self.x += self.z
        scr_x = self.x 
        scr_y = self.y
        return (scr_x, scr_y)
    
    def done(self):
        if self.x > self.scr_width:
            return True
        return False


class Snowflake(Star):
    def __init__(self, screen):
        super().__init__(screen)
        self.radius = 8
        self.noise = PerlinNoise(octaves=8, seed=random.randint(100, 1000))


    def _set_color(self):
        gray_value = 20*self.z
        return (gray_value, gray_value, gray_value)

    def translate(self):
        self.y += self.z
        delta_x = 100 * self.noise(self.y/2000)#self.scr_width)
        scr_x = self.x + delta_x
        scr_y = self.y 
        return (scr_x, scr_y)

    def done(self):
        if self.y > self.scr_height:
            return True
        return False

