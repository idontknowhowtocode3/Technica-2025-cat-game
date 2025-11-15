import pygame


pygame.init()
WIDTH = 1000
HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fat Cat Dash")


def first_House():
    BG = pygame.image.load("Background.jpg")
    WINDOW.blit(BG, (0,0))
    pygame.display.update()


def main():
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
       
        first_House()




    pygame.quit()


if __name__ == "__main__":
    main()

