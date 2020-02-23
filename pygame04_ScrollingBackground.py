import pygame

# initalize pygame modules
pygame.init()
clock = pygame.time.Clock()  # create a clock to control update speed

# create a screen on which to draw
width, height = 500, 300
screensize = [width, height]  # [width, height] in pixels
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('demo04: Scrolling background')   # title of screen window

# initialize font
font = pygame.font.SysFont(None, 16)  # font size = 16

# create a textbox:  red text with white background
text = font.render('Score: %d' %(0), True, (255,255,255), (0,0,0))
textRect = text.get_rect()
textRect.topleft = screen.get_rect().topleft

# import an image to move
image_bg = pygame.image.load(r'Images\starbg.png')

# ready to run game loop
bg_x = 0
bg_speed = 1
score = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if bg_speed < 30:
                bg_speed += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if bg_speed > 1:
                bg_speed -= 1

    screen.fill((255,255,255))  # fill screen with white
    text = font.render('Score: %d' %(score), True, (255,255,255), (0,0,0))
    

    screen.blit(image_bg, (bg_x,0))
    screen.blit(image_bg, (bg_x+600,0)) #screen.blit(fireball, (img_x, img_y)) 
    screen.blit(text, textRect)   # draw text to screen
    pygame.display.update()   # update screen drawing
    bg_x = bg_x - bg_speed
    if bg_x <= -600:
        bg_x = 0
        score += 1

    clock.tick(60)  # advance at 60 fps


