import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GRAY = (200, 200, 200)
BLUE = (100, 149, 237)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Game with QuickSort")

# Load a custom font
font = pygame.font.SysFont("Comic Sans MS", 20)
small_font = pygame.font.SysFont("Comic Sans MS", 16)



# QuickSort function
def quicksort(arr, ascending=True):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot] if ascending else [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot] if ascending else [x for x in arr if x < pivot]
    return quicksort(left, ascending) + middle + quicksort(right, ascending)

# Sorting parameters
order = "ascending"  # Change to "descending" for descending order
numbers = random.sample(range(1, 100), 10)
numbers_sorted = quicksort(numbers, ascending=(order == "ascending"))
current_index = 0  # Track the current index in the sorted list
selected_numbers = []  # Track selected numbers

# Game Messages
def display_message(text, color, y_offset=0):
    message = font.render(text, True, color)
    rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(message, rect)

# Title and instructions
def draw_title_and_instructions():
    title = font.render("Sorting Game: QuickSort Order", True, BLACK)
    instructions = small_font.render("Click the numbers in sorted order.", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))
    screen.blit(instructions, (WIDTH // 2 - instructions.get_width() // 2, 60))

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Draw title and instructions
    draw_title_and_instructions()
    
    # Display numbers as buttons with color-coded feedback
    for idx, num in enumerate(numbers):
        x = 50 + idx * 50
        y = HEIGHT // 2
        color = GREEN if num in selected_numbers else BLUE
        if num == "":
            color = LIGHT_GRAY  # Hide number when clicked
        
        pygame.draw.circle(screen, color, (x, y), 20)
        
        # Draw number text in the circle
        if num != "":
            number_text = font.render(str(num), True, WHITE)
            screen.blit(number_text, (x - 10, y - 10))
    
    # Display selected numbers
    selected_text = small_font.render("Selected: " + " ".join(map(str, selected_numbers)), True, BLACK)
    screen.blit(selected_text, (50, HEIGHT - 120))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for idx, num in enumerate(numbers):
                x = 50 + idx * 50
                y = HEIGHT // 2
                if (x - 20 < mouse_x < x + 20) and (y - 20 < mouse_y < y + 20):
                    if num == numbers_sorted[current_index]:
                        current_index += 1
                        selected_numbers.append(num)  # Track selected number
                        numbers[idx] = ""  # Hide correctly selected number
                        if current_index == len(numbers_sorted):
                            display_message("Completed!", BLACK, 50)
                            pygame.display.flip()
                            pygame.time.delay(2000)
                            running = False
                    else:
                        display_message("Error! Try Again.", RED, 50)
                        pygame.display.flip()
                        pygame.time.delay(1000)

    # Check if completed
    if current_index == len(numbers_sorted):
        display_message("You sorted it correctly!", BLACK, 50)
    
    pygame.display.flip()
