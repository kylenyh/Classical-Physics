# Library imports
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
width, height = 1200, 800  # Expanded window dimensions
bg_color = (255, 255, 255)
ball_color = (0, 0, 255)
ball_radius = 10  # Smaller ball size
font_size = 20  # Font size for details

# Initialize new_velocity
new_velocity = 0

# Create the Pygame window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Inelastic Collision")

# Ball properties
mass_a = 4.2  # Mass of object A (kg)
mass_b = 1.5  # Mass of object B (kg)
vel_a = 3.6   # Initial velocity of object A (m/s)
vel_b = 1.2   # Initial velocity of object B (m/s)

# Initial positions of the balls
pos_a = [100, height // 2]
pos_b = [400, height // 2]

# Initial velocities of the balls
velocities = [vel_a, vel_b]

# Function to calculate kinetic energy
def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

# Initialize tracker variables
mass_a_initial = mass_a
mass_b_initial = mass_b
vel_a_initial = vel_a
vel_b_initial = vel_b
ke_a_initial = kinetic_energy(mass_a, vel_a)
ke_b_initial = kinetic_energy(mass_b, vel_b)
total_ke_initial = ke_a_initial + ke_b_initial
momentum_a_initial = mass_a * vel_a
momentum_b_initial = mass_b * vel_b

# Font for displaying details
font = pygame.font.Font(None, font_size)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Global variable for details_y
details_y = 20

# Function to display details
def display_details(text):
    global details_y
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (20, details_y))
    details_y += font_size

# Variables to track the state of the simulation
collision_occurred = False
balls_stuck = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if the balls are outside the window
    if pos_a[0] + ball_radius < 0 and pos_b[0] - ball_radius > width:
        # Reset positions and velocities for the next simulation
        pos_a = [100, height // 2]
        pos_b = [400, height // 2]
        velocities = [vel_a, vel_b]
        collision_occurred = False
        balls_stuck = False

    if not collision_occurred:
        # Update positions
        pos_a[0] += velocities[0]
        pos_b[0] += velocities[1]

        # Wrap around the window borders
        if pos_a[0] + ball_radius < 0:
            pos_a[0] = width
        if pos_b[0] - ball_radius > width:
            pos_b[0] = -ball_radius

        # Check for collision
        if pos_a[0] + ball_radius >= pos_b[0] - ball_radius:
            # Inelastic collision
            total_mass = mass_a + mass_b
            new_velocity = (mass_a * velocities[0] + mass_b * velocities[1]) / total_mass
            velocities = [new_velocity, new_velocity]

            collision_occurred = True

    elif not balls_stuck:
        # Update positions with the same velocity
        pos_a[0] += new_velocity
        pos_b[0] += new_velocity

        # Check if they reach the end of the window
        if pos_a[0] >= width:
            balls_stuck = True

    # Clear the screen
    screen.fill(bg_color)

    # Draw the balls
    pygame.draw.circle(screen, ball_color, (int(pos_a[0]), int(pos_a[1])), ball_radius)
    pygame.draw.circle(screen, ball_color, (int(pos_b[0]), int(pos_b[1])), ball_radius)

    # Update tracker information
    display_details(f"Initial Mass A: {mass_a_initial} kg")
    display_details(f"Initial Mass B: {mass_b_initial} kg")
    display_details(f"Final Mass A: {mass_a} kg")
    display_details(f"Final Mass B: {mass_b} kg")
    display_details(f"Initial Speed A: {vel_a_initial} m/s")
    display_details(f"Initial Speed B: {vel_b_initial} m/s")
    display_details(f"Final Speed A & B: {new_velocity} m/s")
    display_details(f"Initial KE A: {ke_a_initial} J")
    display_details(f"Initial KE B: {ke_b_initial} J")
    display_details(f"Final KE A: {kinetic_energy(mass_a, new_velocity)} J")
    display_details(f"Final KE B: {kinetic_energy(mass_b, new_velocity)} J")
    display_details(f"Initial Total KE: {total_ke_initial} J")
    display_details(f"Final Total KE: {kinetic_energy(mass_a, new_velocity) + kinetic_energy(mass_b, new_velocity)} J")
    display_details(f"Initial Momentum A: {momentum_a_initial} kg*m/s")
    display_details(f"Initial Momentum B: {momentum_b_initial} kg*m/s")
    display_details(f"Final Momentum A: {mass_a * new_velocity} kg*m/s")
    display_details(f"Final Momentum B: {mass_b * new_velocity} kg*m/s")

    # Reset details_y for displaying details again
    details_y = 20

    # Control the frame rate (60 FPS)
    clock.tick(60)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

