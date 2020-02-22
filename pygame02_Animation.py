import pygame

# initalize pygame modules
pygame.init()
clock = pygame.time.Clock()  # create a clock to control update speed

# create a screen on which to draw
width, height = 500, 400
screensize = [width, height]  # [width, height] in pixels
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('demo02: Basic Annimation')   # title of screen window

# initialize font
font = pygame.font.SysFont(None, 16)  # font size = 16

# create a textbox:  red text with white background
text = font.render('Score: %d' %(0), True, (255,0,0), (255,255,255))
textRect = text.get_rect()
textRect.topleft = screen.get_rect().topleft

# import an image to move
image = pygame.image.load(r'Images\fireball.png')

topx = width//2
topy = height//2
xspeed = 1
yspeed = 1
score = 0

# ready to run game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

    screen.fill((255,255,255))  # fill screen with white
    text = font.render('Score: %d' %(score), True, (0,0,0), (255,255,255))
    screen.blit(text, textRect)   # draw text to screen
    screen.blit(image, (topx, topy)) 
    pygame.display.update()   # update screen drawing

    # update positions
    topx += xspeed
    topy += yspeed
    if topx <= 0 or topx >= width - 32:
        xspeed *= -1
        score += 1
    if topy <= 0 or topy >= height - 32:
        yspeed *= -1
        score += 1

    clock.tick(60)  # advance at 60 fps


