import pygame, random

#sprites
#creates point
class Point(pygame.sprite.Sprite):
    def __init__(self):
        super(Point, self).__init__()
        self.image = pygame.Surface((5,5))
        self.image.fill((255,40,0))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
    def destroy(self):
        pygame.sprite.spritecollide(point, targetGroup, True)
#creates target
class Target(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

#target initialization
def createTarget(smallestTarget, largestTarget):
    if (smallestTarget < 15):
        raise ValueError('Target size is too small.')
    elif (largestTarget > 90):
        raise ValueError('Target size is too large.')
    randSize = random.randrange(smallestTarget, largestTarget)
    target = Target(randSize,randSize,random.randrange(40,1200),random.randrange(40,900),(255,255,0))
    return target

#render score
def renderScore(s):
    if isinstance(s, str):
        raise ValueError('Can only be integer')
    return font.render("Score: " + str(s), 1, (255,40,0))

#render timer
def renderTimer(timer):
    if isinstance(timer, str):
        raise ValueError('Can only be integer')
    return font.render(str(round(timer, 2)), 1, (255,40,0))

#render end screen
def endScreen(score):
    if isinstance(score, str):
        raise ValueError('Can only be integer')
    return font.render("Your final score was " + str(score), 1, (255,40,0))

pygame.init() #initialize game screen
font = pygame.font.Font(None, 74)

if __name__ == '__main__':
    score = 0
    timer = 60
    delta = 0
    running = True
    height = 960
    width = 1440
    smallestTarget = 35
    largestTarget = 75

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
    background = pygame.image.load("background.jpg")
    background = pygame.transform.scale(background,(width,height))
    pygame.mouse.set_visible(False)

    #pointer initialization
    point = Point()
    pointGroup = pygame.sprite.Group()
    pointGroup.add(point)

    t = createTarget(smallestTarget, largestTarget)
    targetGroup = pygame.sprite.Group()
    targetGroup.add(t)

    #game loop
    while running:
        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.collide_rect(point,t):
                point.destroy()
                score += 1
                t = createTarget(smallestTarget, largestTarget)
                targetGroup.add(t)
            elif event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    running = False

        pygame.display.flip()
        screen.blit(background, (0,0)) #display background

        #display timer
        timer -= delta
        text = renderTimer(timer)
        if timer <= 0:
            text = endScreen(score)
            screen.blit(text,(475,360))
        else:
            targetGroup.draw(screen)

            #render time
            screen.blit(text,(40,10))
            delta = clock.tick(30)/1000

            #render score
            text = renderScore(score)
            screen.blit(text,(1200,10))

        #render point
        pointGroup.draw(screen)
        pointGroup.update()

    pygame.quit()
