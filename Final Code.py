import pygame 
# import gif_pygame
# from PIL import Image
import sys
import random

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Fat Cat Dash")
clock = pygame.time.Clock()

# Set up display size
WIDTH = 1000
HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

Cat = pygame.image.load("Cat-removebg.png.png").convert_alpha()
Cat = pygame.transform.scale(Cat,(170,100))

CatR = pygame.image.load("image (3).png").convert_alpha()
Key = pygame.image.load("Key.png").convert_alpha()
Key = pygame.transform.scale(Key,(50,30))

def first_House():
    global escaped
    escaped = False
    global Cat_x
    global Cat_y
    global BG
    global Has_Key
    Has_Key = False

    # Set background and cat GIF
    BG = pygame.image.load("Background.png")

    # Print background and cat on window 
    WINDOW.blit(BG, (0,0))
    WINDOW.blit(Cat,(130,330))
    WINDOW.blit(Key,(175,220))
    pygame.display.update()

    Cat_x = 130
    Cat_y = 330

def second_House():
    global BG
    global Cat_x
    global Cat_y

    global WHITE, BLACK, GREEN, RED
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # Game variables
    global game_active
    game_active = True
    global score
    score = 0
    global font
    font = pygame.font.Font(None, 74)
    global small_font
    small_font = pygame.font.Font(None, 36) 

    # Skill check bar variables

    global bar_width, bar_height, bar_x, bar_y
    bar_width = 400
    bar_height = 20
    bar_x = (WIDTH - bar_width) // 2
    bar_y = (HEIGHT - bar_height) // 2
    global marker_width, marker_speed, marker_direction, marker_x
    marker_width = 10
    marker_speed = 5
    marker_direction = 1
    marker_x = bar_x
    global target_width, target_x
    target_width = 60
    target_x = 0


    BG = pygame.image.load("SecondHouse.png")
    BG = pygame.transform.scale(BG,(1000,800))
    WINDOW.blit(BG,(0,0))
    WINDOW.blit(Cat,(170,500))
    pygame.display.update()

    Cat_x = 130
    Cat_y = 500

def reset_skill_check():
    #resets the minigame and target zone
    global marker_x, marker_direction, target_x, game_active
    marker_x = bar_x
    marker_direction = 1
    #rnadomize the location of the target zone
    target_x = random.randint(bar_x, bar_x + bar_width - target_width)
    game_active = True
    global score, marker_speed
    score = 0
    marker_speed = 5

def check_if_correct():
    #checks if the player clicked in the target zone
    global score, game_active, marker_speed, target_x
    if (target_x <= marker_x <= (target_x + target_width - marker_width)):
        score += 1
        target_x = random.randint(bar_x, bar_x + bar_width - target_width)
        print(f"Success! Score: {score}")
        marker_speed = marker_speed + 1


    else:
        print("Failed!")
        game_active = False

def neighborhood():
    global BG
    global Cat_x
    global Cat_y

    BG = pygame.image.load("map.jpg")
    BG = pygame.transform.scale(BG,(1000,800))
    WINDOW.blit(BG,(0,0))
    WINDOW.blit(Cat,(170,350))
    pygame.display.update()

    Cat_x = 170
    Cat_y = 350
    
    

def user_Movement():
    global Cat_x
    global Cat_y

    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        Cat_y += 1
        WINDOW.blit(BG, (0,0))
        WINDOW.blit(Cat,(Cat_x,Cat_y))
        if (Has_Key == False ):
            WINDOW.blit(Key,(175,230))
        pygame.display.update()

        print(Cat_y)
        
    if key[pygame.K_UP]:
        Cat_y -= 1
        WINDOW.blit(BG, (0,0))
        WINDOW.blit(Cat,(Cat_x,Cat_y))
        if (Has_Key == False ):
            WINDOW.blit(Key,(175,220))
        pygame.display.update()

        print(Cat_y)
    
    if key[pygame.K_LEFT]:
        Cat_x -= 1
        WINDOW.blit(BG, (0,0))
        WINDOW.blit(Cat,(Cat_x,Cat_y))
        if (Has_Key == False ):
            WINDOW.blit(Key,(175,220))
        pygame.display.update()

        print(Cat_x)
        
    if key[pygame.K_RIGHT]:
        Cat_x += 1
        WINDOW.blit(BG, (0,0))
        WINDOW.blit(Cat,(Cat_x,Cat_y))
        if (Has_Key == False ):
            WINDOW.blit(Key,(175,220))
        pygame.display.update()

        print(Cat_x)

def main():
    running = True
    global in_Neighborhood
    in_Neighborhood = False
    first_House()

    while running:
        clock.tick(1000)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            
        user_Movement()

        if (Cat_x in range(130,150) and Cat_y in range(150,200)):
            global Has_Key
            Has_Key = True
            print("You got the Slightly Crispy Key! Now where to use it... ")
            print(Has_Key)

        if (Cat_x in range(820,900) and Cat_y in range(230,880) and Has_Key == True):
            global escaped
            escaped = True
            print("You used the Slightly Crispy Key to unlock the door!")
            print("You've escaped the house!! Now go steal some food.")
        
        if (escaped == True):
            neighborhood()
            escaped = False
            Has_Key = "2"
            in_Neighborhood = True
        
        user_Movement()

        if (in_Neighborhood == True and Cat_x in range(400,450) and Cat_y in range(210,260)):
            second_House()
            print ("House 2")
            in_Neighborhood = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_active:
                check_if_correct()
            else:
                reset_skill_check()

    #game layout logic stuff
    if game_active:
        marker_x += marker_speed * marker_direction
        #reverses the direction if it hits the edges of the bar
        if marker_x <= bar_x or marker_x >= bar_x + bar_width - marker_width:
            marker_direction *= -1
        if score == 5:
            game_active = False
        
        WINDOW.blit("Back.png",(0,0))
        pygame.display.update()

    #draw the game elements
    global score_text
    if game_active == True:
        pygame.draw.rect(WINDOW, WHITE, (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(WINDOW, GREEN, (target_x, bar_y, target_width, bar_height))
        pygame.draw.rect(WINDOW, RED, (marker_x, bar_y, marker_width, bar_height))
        score_text = small_font.render(f"Score: {score}", True, WHITE)
        WINDOW.blit(score_text, (10, 10))
        prompt_text = small_font.render("Click to stop the marker!", True, WHITE)
        WINDOW.blit(prompt_text, (bar_x, bar_y - 40))

        pygame.display.update()


    else:
        #game over screen
        score_text = small_font.render(f"Score: {score}", True, WHITE)


        if score == 5:
            game_over_text = font.render("You Win!", True, WHITE)
            WINDOW.blit(game_over_text, game_over_rect)
            game_active = False
            pygame.display.update()
        else:
            game_over_text = font.render("Game Over", True, WHITE)
            score_text = small_font.render(f"Score: {score}", True, WHITE)
            instructions_text = small_font.render("Click to start a new check", True, WHITE)
       
            game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))


            score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
            instructions_rect = instructions_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))


            WINDOW.blit(game_over_text, game_over_rect)
            WINDOW.blit(score_text, score_rect)
            WINDOW.blit(instructions_text, instructions_rect)     
            game_active = False
            pygame.display.update()


        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
