import random
import pygame

class Star:
    def __init__(self, screen):
        self.screen = screen
        self.scr_width = screen.get_size()[0]
        self.scr_height = screen.get_size()[1]
        self.radius = 1
        self.verlocity = 8
        self.x = random.randint(-self.scr_width/2, self.scr_width/2)
        self.y = random.randint(-self.scr_height/2, self.scr_height/2)
        self.z = random.randint(100, 500)
        self.color = self.__set_color()

    def __set_color(self):
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
        self.z -= self.verlocity
        pygame.draw.circle(self.screen, self.__set_color(), self.translate(), self.radius)

    def translate(self):        
        scr_x = 200*self.x/self.z + self.scr_width / 2
        scr_y = 200*self.y/self.z + self.scr_height / 2
        return (scr_x, scr_y)
    
    def done(self):
        if self.z <= self.verlocity:
            return True
        return False
        
    
