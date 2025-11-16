import pygame
import sys

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Fat Cat Dash")
clock = pygame.time.Clock()

# Set up display size
WIDTH = 1000
HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

Cat = pygame.image.load("Cat-removebg.png.png").convert_alpha()
Cat = pygame.transform.scale(Cat, (270, 200))

# Load the cat (or character) images for animation
cat_frames = []
for i in range(1, 7):  # loads car1.png → car6.png
    img = pygame.image.load(f"car{i}.png").convert_alpha()
    img = pygame.transform.flip(img, True, False) 
    img = pygame.transform.scale(img, (270, 200))  # Resize this maybe
    cat_frames.append(img)

# LEFT SIDE
cat_frames_left = []
for i in range(1, 7):  # loads car1.png → car6.png
    img = pygame.image.load(f"car{i}.png").convert_alpha()
    img = pygame.transform.scale(img, (270, 200))
    cat_frames_left.append(img)

CatR = pygame.image.load("image (3).png").convert_alpha()
Key = pygame.image.load("Key.png").convert_alpha()
Key = pygame.transform.scale(Key, (50, 30))

# Initialize global variables
escaped = False
Cat_x = 130
Cat_y = 330
Has_Key = False
cat_frame_index = 0
cat_animation_speed = 16  # Animation speed control
frame_counter = 0
cat_direction = "right"  # Initial direction


def first_House():
    global escaped, Cat_x, Cat_y, BG, Has_Key
    Has_Key = False

    # Set background and cat GIF
    BG = pygame.image.load("Background.png")

    # Print background and cat on window
    WINDOW.blit(BG, (0, 0))
    WINDOW.blit(Cat, (Cat_x, Cat_y))
    WINDOW.blit(Key, (175, 220))
    pygame.display.update()


def neighborhood():
    global BG, Cat_x, Cat_y
    BG = pygame.image.load("map.jpg")
    BG = pygame.transform.scale(BG, (1000, 800))
    WINDOW.blit(BG, (0, 0))
    WINDOW.blit(Cat, (Cat_x, Cat_y))
    pygame.display.update()


def user_Movement():
    global Cat_x, Cat_y, cat_frame_index, frame_counter, cat_direction, Has_Key

    key = pygame.key.get_pressed()
    moving = False

    if key[pygame.K_DOWN]:
        WINDOW.blit(BG, (0,0))
        Cat_y += 1
        moving = True
    if key[pygame.K_UP]:
        WINDOW.blit(BG, (0,0))
        Cat_y -= 1
        moving = True
    if key[pygame.K_LEFT]:
        WINDOW.blit(BG, (0,0))
        Cat_x -= 1
        moving = True
        cat_direction = "left"
    if key[pygame.K_RIGHT]:
        WINDOW.blit(BG, (0,0))
        Cat_x += 1
        moving = True
        cat_direction = "right"

    # Update animation frame if the cat is moving
    if moving:
        frame_counter += 1
        if frame_counter >= cat_animation_speed:
            frame_counter = 0  # Reset the counter
            cat_frame_index += 1  # Move to the next frame
            if cat_frame_index >= len(cat_frames):
                cat_frame_index = 0  # Loop back to the first frame

    # Draw the current frame of the cat at the current location
    if cat_direction == "right":
        WINDOW.blit(cat_frames[cat_frame_index], (Cat_x, Cat_y))
    else:
        WINDOW.blit(cat_frames_left[cat_frame_index], (Cat_x, Cat_y))

    if not Has_Key:
        WINDOW.blit(Key, (175, 220))

    
    pygame.display.update()


def main():
    global escaped, Has_Key

    running = True
    first_House()

    while running:
        clock.tick(3000)  # Control the frame rate

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        user_Movement()

        # Key pickup condition
        if 130 <= Cat_x <= 150 and 150 <= Cat_y <= 200 and not Has_Key:
            Has_Key = True
            print("You got the Slightly Crispy Key! Now where to use it... ")

        # Escape condition
        if 820 <= Cat_x <= 900 and 230 <= Cat_y <= 880 and Has_Key:
            escaped = True
            print("You used the Slightly Crispy Key to unlock the door!")
            print("You've escaped the house!! Now go steal some food.")

        if escaped:
            neighborhood()
            escaped = False
            Has_Key = False  # Reset the key after escaping

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()