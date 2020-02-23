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

img_x = width//2
img_y = height//2
xspeed = 1
yspeed = 1
score = 0
angle = 0

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
    fireball = pygame.transform.rotate(image,angle);
    img_rect = fireball.get_rect()
    img_rect.centerx = img_x
    img_rect.centery = img_y
    screen.blit(fireball, img_rect)#screen.blit(fireball, (img_x, img_y)) 
    pygame.display.update()   # update screen drawing

    # update positions
    img_x += xspeed
    img_y += yspeed
    angle -= 9
    if angle <= 0:
        angle = 360
    if img_x <= 16 or img_x >= width - 16:
        xspeed *= -1
        score += 1
    if img_y <= 16 or img_y >= height - 16:
        yspeed *= -1
        score += 1

    clock.tick(60)  # advance at 60 fps


