import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1200, 500))
font = pygame.font.SysFont(None, 50)  #None is used if there is no font in our computer so PyGame uses the defualt font; 50 is the size
pygame.display.set_caption("Pong Game")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60
paddle1_y = 200  #top edge of the paddle starts at this height
paddle2_y = 200  
paddle_speed = 7
#AI_paddle_speed = 15

ball_x = 600
ball_y = 250
ball_speed_x = 5 #Ball moves 5 pixels horizontially if the value is positive the ball right if it hits a paddle the value is changed to -5
ball_speed_y = 5 #Similar to ball_speed_x this value will be flipped (multiplied by -1) when the ball bounces off the top or bottom walls.
ball_radius = 10
ball_position = 600

player1_score = 0
player2_score = 0
WINNING_SCORE = 5

running = True
game_Active = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if not game_Active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                #Reset all variables
                player1_score = 0
                player2_score = 0
                ball_x, ball_y = 600, 250
                ball_speed_x, ball_speed_y = 5, 5 #Reset ball speed/direction
                paddle1_y = 200
                paddle2_y = 200
                game_Active = True

    if game_Active:
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_w]: paddle1_y -= paddle_speed
        if keys[pygame.K_s]: paddle1_y += paddle_speed
        if ball_x >= 600:
            if ball_y > (paddle2_y + (90 // 2)): paddle2_y += paddle_speed
            elif ball_y < (paddle2_y + (90 // 2)): paddle2_y -= paddle_speed
            else: paddle2_y

        
    
        if paddle1_y < 0: paddle1_y = 0
        if paddle1_y > 500 - 90: paddle1_y = 410 #Screen_height - paddle_height
        if paddle2_y < 0: paddle2_y = 0
        if paddle2_y > 500 - 90: paddle2_y = 410
    
        ball_x += ball_speed_x
        ball_y += ball_speed_y
    
        if ball_y <= 0 or ball_y >= 500 - ball_radius:
            ball_speed_y *= -1
    
        if ball_x <= 30 and paddle1_y < ball_y < paddle1_y + 90:
            ball_speed_x *= -1
    
        if ball_x >= 1150 and paddle2_y < ball_y < paddle2_y + 90:
            ball_speed_x *= -1
    
        if ball_x < 0:
            player2_score += 1
            ball_x, ball_y = 600, 250
            ball_speed_x *= -1 #Sending the ball to the other player who just won the point.Math magic ㄟ( ▔, ▔ )ㄏ
        
        if ball_x > 1200:
            player1_score += 1
            ball_x, ball_y = 600, 250
            ball_speed_x *= -1

        if player1_score >= WINNING_SCORE or player2_score >= WINNING_SCORE:
            game_Active = False

                                   
    screen.fill(BLACK) 

    if game_Active:
        #(Paddles distance/width from the widows left_screen, W OR S movment depends ont the player, width of paddle, height of paddle)            
        pygame.draw.rect(screen, GREEN, (10, paddle1_y, 20, 90))
    
        #(Paddle distance/width from the widows right_screen, UP or DOWN movment depends ont the player, width of paddle, height of paddle)
        pygame.draw.rect(screen, GREEN, (1170, paddle2_y, 20, 90))
    
        #(surface, color, center_position(here it is tuple specifying the exact center), radius)
        pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), ball_radius)
    
        score1_text = font.render(str(player1_score), True, WHITE)
        score2_text = font.render(str(player2_score), True, WHITE)
        screen.blit(score1_text, (300, 20))
        screen.blit(score2_text, (900, 20))
    
        
    game_over_font = pygame.font.SysFont('impact', 100)
    if not game_Active:
        winner = "YOU Win!" if player1_score >= WINNING_SCORE else "AI Wins!"
        over_text = game_over_font.render(winner, True, RED)
        text_rect = over_text.get_rect(center=(1200 // 2, 500 // 2))
        screen.blit(over_text, text_rect)

        retry_font = pygame.font.SysFont(None, 40)
        retry_text = retry_font.render("Press R to Play Again", True, WHITE)
        retry_rect = retry_text.get_rect(center=(1200 // 2, 500 // 2 + 100))
        screen.blit(retry_text, retry_rect)


    pygame.display.flip()
    clock.tick(FPS)