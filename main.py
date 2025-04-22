import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Genetic Algorithm Racing Car")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
lightblue = (173, 216, 230)
lightgreen = (144, 238, 144)

# Game parameters
default_rotate_value = 3
default_speed_increment = 0.015
default_speed_start = 0.4
time_count = 0
car_x = 130
car_y = 65
line_length = 30
angle = 0
speed = default_speed_start
bane_image = None
aktuel_color = black

# Genetic Algorithm parameters
population = []
population_number = 30
number_of_genes_in_chromosome = 8
active_population = -1
max_time_per_game = 3000

# Load track image
try:
    bane_image = pygame.image.load('bane.png')
except pygame.error as e:
    print(f"Error loading 'bane.png': {e}")
    pygame.quit()
    exit()

def get_random_number(decimal_places, size):
    scale = 10**decimal_places
    return round((random.random() - 0.5) * size, decimal_places)

def rotate_car(left_right):
    global angle
    angle += left_right / 10
    if angle > 360:
        angle -= 360
    elif angle < 0:
        angle += 360

def speed_change(speed_in):
    global speed
    speed += speed_in / 1000

def line_to_angle(x1, y1, length, angle_rad):
    x2 = x1 + length * math.cos(angle_rad)
    y2 = y1 + length * math.sin(angle_rad)
    return (int(x2), int(y2))

def just_infront_forward_distance():
    length = 10
    angle_rad = math.radians(angle)
    x2 = car_x + length * math.cos(angle_rad)
    y2 = car_y + length * math.sin(angle_rad)
    return (int(x2), int(y2))

def get_distance(check_angle_offset):
    length = 5
    angle_rad = math.radians(angle + check_angle_offset)
    start_x, start_y = just_infront_forward_distance()
    for i in range(200):
        x2 = int(start_x + length * math.cos(angle_rad))
        y2 = int(start_y + length * math.sin(angle_rad))
        if 0 <= x2 < screen_width and 0 <= y2 < screen_height:
            pixel_color = screen.get_at((x2, y2))
            if pixel_color[1] < 200:  # Check green component
                break
        else:
            break # Out of screen bounds
        length += 5
    return (x2, y2)

def forward():
    global car_x, car_y
    angle_rad = math.radians(angle)
    dx = speed * math.cos(angle_rad)
    dy = speed * math.sin(angle_rad)
    car_x += dx
    car_y += dy

def backward():
    global car_x, car_y, speed
    angle_rad = math.radians(angle)
    dx = -speed * math.cos(angle_rad)
    dy = -speed * math.sin(angle_rad)
    car_x += dx
    car_y += dy

def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def draw_everything():
    screen.blit(bane_image, (0, 0))

    angle_rad = math.radians(angle)

    # Calculating car corners
    length_minus_15 = line_length - 15
    length_minus_10 = line_length - 10

    angle1_rad = math.radians(angle + 240) if angle + 240 <= 360 else math.radians(angle - 120)
    new_pos1 = line_to_angle(car_x, car_y, length_minus_15, angle1_rad)

    angle2_rad = angle_rad
    new_pos2 = line_to_angle(car_x, car_y, length_minus_10, angle2_rad)

    angle3_rad = math.radians(angle + 120) if angle + 120 <= 360 else math.radians(angle - 240)
    new_pos3 = line_to_angle(car_x, car_y, length_minus_15, angle3_rad)

    # Drawing distance sensors
    start_point = just_infront_forward_distance()

    dist_forward_end = get_distance(0)
    pygame.draw.line(screen, lightblue, start_point, dist_forward_end, 1)
    distant_front = dist(start_point[0], start_point[1], dist_forward_end[0], dist_forward_end[1])

    dist_left_end = get_distance(-70)
    pygame.draw.line(screen, lightgreen, start_point, dist_left_end, 1)
    distant_left = dist(start_point[0], start_point[1], dist_left_end[0], dist_left_end[1])

    dist_right_end = get_distance(70)
    pygame.draw.line(screen, red, start_point, dist_right_end, 1)
    distant_right = dist(start_point[0], start_point[1], dist_right_end[0], dist_right_end[1])

    # Drawing the car
    pygame.draw.polygon(screen, aktuel_color, [new_pos1, new_pos2, new_pos3], 2)

    # Draw Text
    font = pygame.font.Font(None, 20)
    text_controls = font.render("Left='a' Right='d' Fast='w' Slow='s'", True, black)
    screen.blit(text_controls, (310, 20))

    text_car_pos = font.render(f"Car x = {car_x:.0f} Car y = {car_y:.0f}", True, black)
    screen.blit(text_car_pos, (350, 60))
    text_dist_front = font.render(f"Distance front = {distant_front:.0f}", True, black)
    screen.blit(text_dist_front, (350, 80))
    text_dist_left = font.render(f"Distance left = {distant_left:.0f}", True, black)
    screen.blit(text_dist_left, (350, 100))
    text_dist_right = font.render(f"Distance right = {distant_right:.0f}", True, black)
    screen.blit(text_dist_right, (350, 120))
    text_time = font.render(f"Time = {time_count}", True, black)
    screen.blit(text_time, (350, 140))
    text_speed = font.render(f"Speed = {speed:.2f}", True, black)
    screen.blit(text_speed, (350, 160))

    return distant_front, distant_left, distant_right

def check_collision():
    if 0 <= int(car_x) < screen_width and 0 <= int(car_y) < screen_height:
        pixel_color = screen.get_at((int(car_x), int(car_y)))
        # Assuming your circle is a specific color (e.g., black)
        circle_color = (0, 0, 0)  # Change this to the actual color of your circle
        if pixel_color == circle_color:
            return True
    return False

def ga_drive_car_one_time_step(distant_front, distant_left, distant_right):
    global car_x, car_y, aktuel_color

    if time_count > max_time_per_game:
        car_x = -100 # Move car off-screen to stop
        car_y = -100
        return

    try:
        # Use the first individual in the population for now
        if population:
            out_rotate = population[0]['chromosome'][0] * default_rotate_value # Scale the gene
            out_speed_change = population[0]['chromosome'][1] * default_speed_increment * 100 # Scale the gene

            rotate_car(out_rotate)
            speed_change(out_speed_change)

            draw_status()
    except IndexError:
        print("Population is empty!")
    except Exception as e:
        print(f"Error in GA_DriveCar: {e}")

def ga_create_new_population():
    global population
    print("New Population created")
    population = []
    for _ in range(population_number):
        chromosome = [get_random_number(2, 1) for _ in range(number_of_genes_in_chromosome)]
        population.append({'chromosome': chromosome, 'fitness': 0, 'fitness_in_percent': 0})

def car_crashed():
    global aktuel_color, running, game_started
    font = pygame.font.Font(None, 40)
    text = font.render("Car has crashed!", True, red)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(1000)
    start_new_game() # Restart the game after crash

def draw_status():
    font = pygame.font.Font(None, 20)
    text = font.render(f"Active population = {active_population + 1} of {population_number}", True, black)
    screen.blit(text, (200, 380))
    pygame.display.flip() # Update the display to show the text

def show_start_button():
    global running
    button_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 - 30, 200, 60)
    button_color = green
    text_color = white
    font = pygame.font.Font(None, 40)
    text = font.render("Start Learning", True, text_color)
    text_rect = text.get_rect(center=button_rect.center)

    while not game_started and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    start_new_game()

        screen.fill(white)
        pygame.draw.rect(screen, button_color, button_rect)
        screen.blit(text, text_rect)
        pygame.display.flip()

def start_new_game():
    global car_x, car_y, angle, speed, time_count, aktuel_color, game_started
    car_x = 130
    car_y = 65
    angle = 0
    speed = default_speed_start
    time_count = 0
    aktuel_color = black
    ga_create_new_population()
    game_started = True

# Game loop
running = True
game_started = False
show_start_button()

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_started:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    speed += default_speed_increment
                if event.key == pygame.K_s:
                    speed -= default_speed_increment
                if event.key == pygame.K_a:
                    rotate_car(-default_rotate_value)
                if event.key == pygame.K_d:
                    rotate_car(default_rotate_value)

    if game_started:
        forward()
        distant_front, distant_left, distant_right = draw_everything()
        time_count += 1
        ga_drive_car_one_time_step(distant_front, distant_left, distant_right)

        if check_collision():
            aktuel_color = red
            draw_everything()
            pygame.display.flip()
            pygame.time.delay(50) # Small delay to show red before crash message
            car_crashed()

        pygame.display.flip()

    clock.tick(50) # Limit frame rate to around 50 FPS (adjust as needed)

pygame.quit()