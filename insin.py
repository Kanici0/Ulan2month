import pygame
from pygame import mixer

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Pygame game')
icon = pygame.image.load('images/color.jpeg')
pygame.display.set_icon(icon)


plays = pygame.image.load('images/gema.jpg')

wal_left = [
    # pygame.image.load('images/загрузк-removebg-preview (1).png'),
    # pygame.image.load('images/загрузк-removebg-preview (2).png'),
    # pygame.image.load('images/загрузк-removebg-preview (3).png'),
    # pygame.image.load('images/загрузк-removebg-preview (4).png'),
    # pygame.image.load('images/загрузк-removebg-preview (6).png'),
    # pygame.image.load('images/image24-removebg-preview (2).png'),
    # pygame.image.load('images/загрузк-removebg-preview (7).png'),
    # pygame.image.load('images/загрузк-removebg-preview (8).png'),
    # pygame.image.load('images/загрузк-removebg-preview (9).png'),
    # pygame.image.load('images/image24-removebg-preview.png'),
    # pygame.image.load('images/image24-removebg-preview (1).png'),
    # pygame.image.load('images/image24-removebg-preview (2).png'),
    # pygame.image.load('images/image24-removebg-preview (3).png'),
    # pygame.image.load('images/image24-removebg-preview (4).png'),
    pygame.image.load('images/image24-removebg-preview.png'),
    pygame.image.load('images/image24-removebg-preview (1).png'),
    pygame.image.load('images/image24-removebg-preview (2).png'),
    pygame.image.load('images/image24-removebg-preview (3).png'),
    pygame.image.load('images/image24-removebg-preview (4).png')
]
wal_right = [pygame.image.load('images/image24-removebg-preview.png'),
    pygame.image.load('images/image24-removebg-preview (1).png'),
    pygame.image.load('images/image24-removebg-preview (2).png'),
    pygame.image.load('images/image24-removebg-preview (3).png'),
    pygame.image.load('images/image24-removebg-preview (4).png')
]

peler_anim = 1
bj = 0

plear_sped = 5
plear_x = 150
# is_jamp = False
# jamp = 7

ren = True

cloo = mixer.Sound('images/f0cfb0928390cfe.mp3')
cloo.play(-1)

while ren:
    screen.blit(plays, (bj, 0))
    screen.blit(plays, (bj , 0))
    # if keys[pygame.K_LEFT]:
    screen.blit(wal_left[peler_anim], (plear_x, 220))

    # else:
    #     screen.blit(wal_right[peler_anim], (plear_x, 220))
    #

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and plear_x >50:
        plear_x -= plear_sped

    elif keys[pygame.K_RIGHT] and plear_x < 200:
        plear_x += plear_sped

    if peler_anim == 3:
        peler_anim = 0
    else:
        peler_anim += 1


    bj -= 0
    if bj == -611:
        bj = 0

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ren = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                ren = False
                pygame.quit()





    clock.tick(2)
