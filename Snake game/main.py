import pygame
import random
import sys

pygame.init()

# Window
screen = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("Snake game")

# Colors
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255, 255, 255)

#Snake Body and Food
snake_body = [(100,50),(90,50),(80,50),(70,50)]
direction = "RIGHT"
food_position = (random.randrange(0, 1200, 10), random.randrange(0, 500, 10))
score = 0
game_over = False
font = pygame.font.SysFont("arial", 30)

# Clock
clock = pygame.time.Clock()
speed = 15


#Function to Display Text
def draw (text,color,x,y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface,(x,y))

#Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
    #Movement
    if not game_over:
        head_x, head_y = snake_body[0]

        if direction == "RIGHT":
            head_x += 10
        elif direction == "LEFT":
            head_x -= 10
        elif direction == "UP":
            head_y -= 10
        elif direction == "DOWN":
            head_y += 10

    new_head = (head_x, head_y)
    snake_body.insert(0, new_head)
    
    #Game Over Condition
    if head_x < 0 or head_x >= 1200 or head_y < 0 or head_y >= 500:
        game_over = True
    
    if new_head in snake_body[1:]:
        game_over = True

    # Check food
    if new_head == food_position:
        score += 10
        food_position = (random.randrange(0, 1200, 10),
                          random.randrange(0, 500, 10))
        speed += 1
    else:
        snake_body.pop()

    # Draw everything
    screen.fill(BLACK)
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], 10, 10))


    pygame.draw.rect(screen, RED, pygame.Rect(food_position[0], food_position[1], 10, 10))

    draw(f"Score: {score}",WHITE, 10, 10)
    
    #Game Over
    if game_over:
        draw("GAME OVER!", RED, 1200 // 2 - 85, 500 // 2 - 40)
        draw(f"Your Score: {score}",WHITE, 1200 // 2 - 85, 500 // 2)

    pygame.display.update()
    clock.tick(speed)




