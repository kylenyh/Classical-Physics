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
pygame.display.set_caption("Elastic Collision")

# Ball properties
mass_a = 4.0  # Mass of ball A (kg)
mass_b = 2.0  # Mass of ball B (kg)
vel_a_initial = 5.0   # Initial velocity of ball A (m/s)
vel_b_initial = 0.0   # Initial velocity of ball B (m/s)
vel_a_final = 1.67   # Final velocity of ball A (m/s)
vel_b_final = 6.67   # Final velocity of ball B (m/s)

# Initial positions of the balls
pos_a = [100, height // 2]
pos_b = [400, height // 2]

# Initial velocities of the balls
velocities = [vel_a_initial, vel_b_initial]

# Function to calculate kinetic energy
def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

# Initialize tracker variables
ke_a_initial = kinetic_energy(mass_a, vel_a_initial)
ke_b_initial = kinetic_energy(mass_b, vel_b_initial)
total_ke_initial = ke_a_initial + ke_b_initial
momentum_a_initial = mass_a * vel_a_initial
momentum_b_initial = mass_b * vel_b_initial

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

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not collision_occurred:
        # Update positions
        pos_a[0] += velocities[0]
        pos_b[0] += velocities[1]

        # Check for collision
        if pos_a[0] + ball_radius >= pos_b[0] - ball_radius:
            # Elastic collision
            new_velocity_a = ((mass_a - mass_b) / (mass_a + mass_b)) * vel_a_initial + ((2 * mass_b) / (mass_a + mass_b)) * vel_b_initial
            new_velocity_b = ((2 * mass_a) / (mass_a + mass_b)) * vel_a_initial + ((mass_b - mass_a) / (mass_a + mass_b)) * vel_b_initial
            velocities = [new_velocity_a, new_velocity_b]

            collision_occurred = True

    # Clear the screen
    screen.fill(bg_color)

    # Draw the balls
    pygame.draw.circle(screen, ball_color, (int(pos_a[0]), int(pos_a[1])), ball_radius)
    pygame.draw.circle(screen, ball_color, (int(pos_b[0]), int(pos_b[1])), ball_radius)

    if collision_occurred:
        # Update positions based on final velocities
        pos_a[0] += new_velocity_a
        pos_b[0] += new_velocity_b

    # Update tracker information
    display_details(f"Initial Mass A: {mass_a} kg")
    display_details(f"Initial Mass B: {mass_b} kg")
    display_details(f"Initial Speed A: {vel_a_initial} m/s")
    display_details(f"Initial Speed B: {vel_b_initial} m/s")

    if collision_occurred:
        display_details(f"Final Speed A: {new_velocity_a:.2f} m/s")
        display_details(f"Final Speed B: {new_velocity_b:.2f} m/s")

    display_details(f"Initial KE A: {ke_a_initial:.2f} J")
    display_details(f"Initial KE B: {ke_b_initial:.2f} J")

    if collision_occurred:
        display_details(f"Final KE A: {kinetic_energy(mass_a, new_velocity_a):.2f} J")
        display_details(f"Final KE B: {kinetic_energy(mass_b, new_velocity_b):.2f} J")

    display_details(f"Initial Total KE: {total_ke_initial:.2f} J")

    if collision_occurred:
        display_details(f"Final Total KE: {kinetic_energy(mass_a, new_velocity_a) + kinetic_energy(mass_b, new_velocity_b):.2f} J")

    display_details(f"Initial Momentum A: {momentum_a_initial:.2f} kg*m/s")
    display_details(f"Initial Momentum B: {momentum_b_initial:.2f} kg*m/s")

    if collision_occurred:
        display_details(f"Final Momentum A: {mass_a * new_velocity_a:.2f} kg*m/s")
        display_details(f"Final Momentum B: {mass_b * new_velocity_b:.2f} kg*m/s")

    # Reset details_y for displaying details again
    details_y = 20

    # Control the frame rate (60 FPS)
    clock.tick(60)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
