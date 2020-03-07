from src.constants import *

charSprites = pygame.sprite.Group()
itemSprites = pygame.sprite.Group()
bulletSpritesPlayer = pygame.sprite.Group()
bulletSpritesEnemy = pygame.sprite.Group()
platformSprites = pygame.sprite.Group()

class Gravity():
    def __init__(self, acc, vel):
        self.accGravity = acc
        self.velGravity = vel

    # returns True if entity is colliding with ground
    def update(self, entity):
        contact = False

        # Applies gravity
        if entity.rect.y < SCREEN_HEIGHT - entity.rect.height - self.velGravity:
            entity.rect.move_ip(0, self.velGravity)
            self.velGravity += self.accGravity
        else:
            # Contact with ground
            self.velGravity = 0
            contact = True

        return contact



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/sprites/newBoss.png")
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH / 2
        self.rect.y = SCREEN_HEIGHT / 2

        self.deathCount = 0
        self.player_status = False

        self.gravity = Gravity(0.5, 0)

        self.pressedJump = False
        self.velJump = 20

        self.killCount = 0
        self.shotsFired = 0

        self.damageDealt = 0


    def setStatus(self, status):
        self.player_status = status

    def isDead(self):
        if self.player_status == True:
            self.deathCount += 1

    def queryDeathCount(self):
        return self.deathCount



    def update(self, dt):
        pressed = pygame.key.get_pressed()
        # dt is current FPS; movement updates every FPS/dividend frames; change dividend to change base movement speed
        move = dt / 3

        # Handles player movement (WASD)
        if pressed[pygame.K_w] and not self.pressedJump:
            self.pressedJump = True
        if pressed[pygame.K_a]:
            if self.rect.x > -move: self.rect.move_ip(-move, 0)
        if pressed[pygame.K_s]:
            if self.rect.y < SCREEN_HEIGHT - self.rect.height + move: self.rect.move_ip(0, move)
        if pressed[pygame.K_d]:
            if self.rect.x < SCREEN_WIDTH - self.rect.width + move: self.rect.move_ip(move, 0)

        # Jump with W
        if self.pressedJump:
            self.rect.move_ip(0, -self.velJump)
            self.velJump -= self.gravity.accGravity

        if self.gravity.update(self):
            self.pressedJump = False
            self.velJump = 30

        # Border collision
        if self.rect.y <= -move: self.rect.move_ip(0, move)
        if self.rect.x <= -move: self.rect.move_ip(move, 0)
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height + move: self.rect.move_ip(0, -move)
        if self.rect.x >= SCREEN_WIDTH - self.rect.width + move: self.rect.move_ip(-move, 0)


class Gun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/sprites/desert_hawk.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        # Position relative to player (NOT the actual coordinate position of gun); used as direction
        self.pos = pygame.Vector2(-1, 0)

        # Rotating images by angles not divisible by 90 auto-pads image; avoid using rotate
        self.imageEast = self.image
        self.imageWest = pygame.transform.flip(self.image, 1, 0)

        self.shootDelay = 200
        self.lastShotTime = pygame.time.get_ticks()

    def shoot(self):
        self.shot
        pressed = pygame.key.get_pressed()
        currentTime = pygame.time.get_ticks()
        if (pressed[pygame.K_UP] or pressed[pygame.K_LEFT] or pressed[pygame.K_DOWN] or pressed[pygame.K_RIGHT]) \
                and currentTime - self.lastShotTime > self.shootDelay:
            bullet = Bullet(self.rect.x, self.rect.y, self.pos)
            bulletSpritesPlayer.add(bullet)
            self.lastShotTime = currentTime


    def update(self, dt, playerX, playerY):
        pressed = pygame.key.get_pressed()
        # dt is current FPS; movement updates every FPS/dividend frames; change dividend to change base movement speed
        move = dt / 5

        # Moves gun with player (WASD)
        if not pressed[pygame.K_UP] and not pressed[pygame.K_LEFT] and not pressed[pygame.K_DOWN] and not pressed[
            pygame.K_RIGHT]:
            if pressed[pygame.K_w]:
                self.rect.move_ip(0, -move)
                self.pos += (0, -1)
            if pressed[pygame.K_a]:
                self.rect.move_ip(-move, 0)
                self.pos += (-1, 0)
                self.image = self.imageWest
            if pressed[pygame.K_s]:
                self.rect.move_ip(0, move)
                self.pos += (0, 1)
            if pressed[pygame.K_d]:
                self.rect.move_ip(move, 0)
                self.pos += (1, 0)
                self.image = self.imageEast

        # Moves gun when aiming (Arrow keys)
        if pressed[pygame.K_UP]:
            self.pos += (0, -1)
        if pressed[pygame.K_LEFT]:
            self.pos += (-1, 0)
            if not pressed[pygame.K_RIGHT]:
                self.image = self.imageWest
        if pressed[pygame.K_DOWN]:
            self.pos += (0, 1)
        if pressed[pygame.K_RIGHT]:
            self.pos += (1, 0)
            if not pressed[pygame.K_LEFT]:
                self.image = self.imageEast

        # Prevents divide zero normalization error and gun flying off bug
        if self.pos[0] + self.pos[1] == 0:
            self.pos += (1, 1)

        # Normalization ensures consistent movement
        pygame.Vector2.normalize_ip(self.pos)

        # Yeah just do it mate
        self.shoot()

        # Adjust num in (self.pos[i] * num) for distance from player
        self.rect.x = playerX + (self.pos[0] * 50)
        self.rect.y = playerY + (self.pos[1] * 50)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load('resources/sprites/blockade.png')
        self.rect = self.image.get_rect()
    def setPos(self, x, y):
        self.rect.x = x
        self.rect.y = y
    '''
    Argument: Sprite class -> rect -> (x,y)
    '''
    def detectCollison(self, entity):
        collision_list = pygame.sprite.spritecollide(entity, platformSprites, dokill=False, collided=None)

        for collided_objects in collision_list:
            if entity.rect.y > collided_objects.rect.y:
                print('collide')
                #player moves up (cant go thru)

            if entity.rect.y < (collided_objects.rect.y - entity.rect.y):
                print('collide')

        return collision_list

class Bullet(pygame.sprite.Sprite):
    # Reminder that Python passes by object reference; when 'direction' changes in class Gun(),
    # the value in class Bullet() changes as well, changing direction of all bullets;
    # prevent this by making separate variables dirX and dirY

    # Constructor take parameters x and y position to spawn at; determines direction to shoot (used in Gun.shoot())
    def __init__(self, initX, initY, direction):
        super().__init__()
        self.image = pygame.image.load("resources/sprites/newBoss.png")
        self.rect = self.image.get_rect()
        self.rect.x = initX
        self.rect.y = initY
        # Force pass by value by making two separate variables to store X and Y direction
        self.dirX = direction[0]
        self.dirY = direction[1]

        self.numBounces = 0


    def update(self, dt):
        move = dt / 2

        # Hit top and bottom borders
        if self.rect.y <= -move or self.rect.y >= SCREEN_HEIGHT - self.rect.height + move:
            self.dirY *= -1
            self.numBounces += 1
        # Hit left and right borders
        if self.rect.x <= -move or self.rect.x >= SCREEN_WIDTH - self.rect.width + move:
            self.dirX *= -1
            self.numBounces += 1

        if self.numBounces == 2:
            self.kill()

        self.rect.move_ip(self.dirX * move, self.dirY * move)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/sprites/aiPlayer.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = SCREEN_HEIGHT / 2

        self.velY = -1

        self.shootDelay = 500
        self.lastShotTime = pygame.time.get_ticks()

    def update(self, dt):
        move = dt / 5

        if self.rect.y > -move or self.rect.y < SCREEN_HEIGHT - self.rect.height + move:
            self.rect.move_ip(0, self.velY * move)
        if self.rect.y <= -move or self.rect.y >= SCREEN_HEIGHT - self.rect.height + move:
            self.velY *= -1

        self.attack()

    def attack(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastShotTime > self.shootDelay:
            bullet = Bullet(self.rect.x, self.rect.y, (1, 0))
            bulletSpritesPlayer.add(bullet)
            self.lastShotTime = currentTime
