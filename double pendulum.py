
# Library imports
import pygame
import math
 
pygame.init()

# Window dimensions
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Double Pendulum Simulation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Pendulum:
    def __init__(self, length, mass, angle, ang_vel, pivot):
        self.length = length
        self.mass = mass
        self.angle = angle
        self.ang_vel = ang_vel
        self.pivot = pivot
    
    def update(self, gravity, time):
        ang_acc = -gravity / self.length * math.sin(self.angle)
        self.ang_vel += ang_acc * time
        self.angle += self.ang_vel * time

    def draw(self, screen):
        bob_x = self.pivot[0] + self.length * math.sin(self.angle)
        bob_y = self.pivot[1] + self.length * math.cos(self.angle)
        pygame.draw.line(screen, WHITE, self.pivot, (bob_x, bob_y), 2)
        pygame.draw.circle(screen, RED, (int(bob_x), int(bob_y)), 4)

class DoublePendulum:
    def __init__(self, length1, mass1, length2, mass2, initial_angles, initial_velocities):
        self.pendulum1 = Pendulum(length1, mass1, initial_angles[0], initial_velocities[0], (width // 2, height // 2))
        self.pendulum2 = Pendulum(length2, mass2, initial_angles[1], initial_velocities[1], (0, 0))  # Initialize piv_x and piv_y
    
    def update(self, gravity, time):
        self.pendulum1.update(gravity, time)
        self.pendulum2.update(gravity, time)

    def draw(self, screen):
        self.pendulum1.draw(screen)
        self.pendulum2.pivot = (self.pendulum1.length * math.sin(self.pendulum1.angle) + self.pendulum1.pivot[0], 
                                self.pendulum1.length * math.cos(self.pendulum1.angle) + self.pendulum1.pivot[1])
        self.pendulum2.draw(screen)

clock = pygame.time.Clock()
gravity = 9.8
time_step = 0.2

# Set up double pendulum
initial_angles = [math.pi / 2, math.pi / 2]  # Initial angles for both pendulums
initial_velocities = [0, 1]  # Initial angular velocities for both pendulums
double_pendulum = DoublePendulum(100, 20, 120, 20, initial_angles, initial_velocities)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    window.fill(BLACK)
    
    double_pendulum.update(gravity, time_step)
    double_pendulum.draw(window)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

