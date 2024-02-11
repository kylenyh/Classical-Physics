# Library imports
import pygame
import math 

pygame.init()

w_screen = 900
w_height = 400
pygame.display.set_caption('Classical Single Pendulum Simulation')
window = pygame.display.set_mode((w_screen, w_height))
clock = pygame.time.Clock()

# Colors
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Pendulum parameters
piv_x = 500 # X-coordinate of the pivot point
piv_y = 80  # Y-coordinate of the pivot point
l = 300  # Length of the pendulum
angle = math.pi / 3  # Initial angle (in radians)
ang_vel = 0  # Initial angular velocity
gravity = 9.8  # Acceleration due to gravity
time = 0.5 # Time 

class Pendulum:
    def __init__(self, piv_x, piv_y, l, angle, ang_vel):
        self.pivot_x = piv_x
        self.pivot_y = piv_y
        self.l = l
        self.angle = angle
        self.ang_vel = ang_vel

    def update(self):
        ang_acc = -gravity / self.l * math.sin(self.angle)
        self.ang_vel += ang_acc * time
        self.angle += self.ang_vel * time

    def display(self):
        bob_x = self.pivot_x + self.l * math.sin(self.angle)
        bob_y = self.pivot_y + self.l * math.cos(self.angle)
        pygame.draw.line(window, black, (self.pivot_x, self.pivot_y), (bob_x, bob_y), 5)
        pygame.draw.circle(window, red, (int(bob_x), int(bob_y)), 20)

pendulum = Pendulum(piv_x, piv_y, l, angle, ang_vel)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pendulum.update()

    # Clear the window
    window.fill(white)

    pendulum.display()

    # Update the display
    pygame.display.update()

    # Set the desired frame rate
    clock.tick(100)

# Quit Pygame
pygame.quit()

