import pygame

# initalize pygame modules
pygame.init()
clock = pygame.time.Clock()  # create a clock to control update speed

# create a screen on which to draw
screensize = [300, 200]  # [width, height] in pixels
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('demo01: Hello World')   # title of screen window

# initialize font
font = pygame.font.SysFont(None, 40)  # font size = 40

# create a textbox:  red text with white background
text = font.render('    Hello world!', True, (255,0,0), (255,255,255))
textRect = text.get_rect()
textRect.centerx = screen.get_rect().centerx
textRect.centery = screen.get_rect().centery

# ready to run game loop
red = 255
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

    screen.fill((255,255,255))  # fill screen with white
    text = font.render('%003d Hello world!' %(red), True, (red,0,0), (255,255,255))
    screen.blit(text, textRect)   # draw text to screen
    pygame.display.update()   # update screen drawing
    red -= 1
    if red <= 0:
        red = 255
    clock.tick(60)  # advance at 60 fps

