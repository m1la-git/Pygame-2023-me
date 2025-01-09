import pygame as pg
import random

vec = pg.math.Vector2


class Button(pg.sprite.Sprite):
    def __init__(self, img, scale, x, y):
        super(Button, self).__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self, screen):
        action = False
        pos = pg.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] and not self.clicked:
                action = True
                self.clicked = True

            if not pg.mouse.get_pressed()[0]:
                self.clicked = False

        screen.blit(self.image, self.rect)
        return action


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load('images/money.png'), (w, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.transform.scale(pg.image.load('images/front.png'), (60, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.fall = False

    def jump(self):
        if pg.sprite.spritecollide(self, platforms, False):
            self.vel.y = -20
            random.choice([jump_sound1, jump_sound2]).play()

    def update(self):
        self.acc = vec(0, 0.8)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -0.5
            self.image = pg.transform.scale(pg.image.load('images/left.png'), (60, 80))
        elif keys[pg.K_RIGHT]:
            self.acc.x = 0.5
            self.image = pg.transform.scale(pg.image.load('images/right.png'), (60, 80))
        else:
            if player.vel.y <= 0:
                self.image = pg.transform.scale(pg.image.load('images/front.png'), (60, 80))
            else:
                self.image = pg.transform.scale(pg.image.load('images/scream.png'), (60, 80))

        self.acc.x += self.vel.x * (-0.12)

        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos


WIDTH = 480
HEIGHT = 650

running = True
score = 0

pg.init()

pg.display.set_caption('KAMILA CAREER')
screen = pg.display.set_mode((WIDTH, HEIGHT))

bg = pg.transform.scale(pg.image.load('images/bg.png'), (WIDTH, HEIGHT))
win = pg.transform.scale(pg.image.load('images/win.jpg'), (180, 240))
lose = pg.transform.scale(pg.image.load('images/lose.jpg'), (180, 240))
picture = lose

pg.mixer.music.load('sounds/dummy.mp3')
pg.mixer.music.set_volume(0.7)
pg.mixer.music.play(loops=-1)
jump_sound1 = pg.mixer.Sound('sounds/jump1.wav')
jump_sound2 = pg.mixer.Sound('sounds/jump2.wav')
scream = pg.mixer.Sound('sounds/scream.wav')


clock = pg.time.Clock()

font = pg.font.Font('fonts/Pillowtalk.otf', 50)
font_end = pg.font.Font('fonts/Pillowtalk.otf', 100)

all_sprites = pg.sprite.Group()
platforms = pg.sprite.Group()
player = Player(screen)
all_sprites.add(player)

restart_button = Button(pg.transform.scale(pg.image.load('images/restart.png'), (80, 80)), (1, 1), 350, 150)

PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH), (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100), (125, HEIGHT - 350, 100),
                 (350, 200, 100), (175, 100, 50)]
text = ''
best_score = 0
for plat in PLATFORM_LIST:
    p = Platform(*plat)
    all_sprites.add(p)
    platforms.add(p)
playing = True
bg_y1 = 0
bg_y2 = -HEIGHT
scream_sound_wasnt = True
lost = False
while running:
    player.fall = False
    screen.blit(bg, (0, bg_y1))
    screen.blit(bg, (0, bg_y2))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            playing = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()

    if playing:
        all_sprites.update()
        if player.vel.y > 0:
            hits = pg.sprite.spritecollide(player, platforms, False)
            if hits:
                player.pos.y = hits[0].rect.top
                player.vel.y = 0
        if player.rect.top <= HEIGHT / 4:
            player.pos.y += abs(player.vel.y)

            bg_y1 += abs(player.vel.y) // 1.2
            if bg_y1 > HEIGHT:
                bg_y1 = bg_y1 - HEIGHT
            bg_y2 = bg_y1 - HEIGHT
            for plat in platforms:
                plat.rect.y += abs(player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    score += 10
        if player.rect.bottom > HEIGHT:
            if scream_sound_wasnt:
                scream.play()
                scream_sound_wasnt = False
            bg_y1 -= max(player.vel.y, 10) // 1.2
            if bg_y1 < 0:
                bg_y1 = bg_y1 + HEIGHT
            bg_y2 = bg_y1 - HEIGHT
            for sprite in all_sprites:
                sprite.rect.y -= max(player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(platforms) == 0:
            playing = False
            lost = True

        while len(platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, WIDTH - width),
                         random.randrange(-75, -30),
                         width)
            platforms.add(p)
            all_sprites.add(p)

        all_sprites.draw(screen)
        text_surface = font.render(str(score), True, '#006400')
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2, 15)
        screen.blit(text_surface, text_rect)
    else:
        if lost:
            if best_score >= score:
                text = 'Game Over.'
                lost = False
                picture = lose
            else:
                best_score = score
                text = 'Congrats!'
                lost = False
                picture = win
        screen.blit(picture, (50, 350))
        screen.blit(font_end.render(text, True, '#006400'), (50, 50))
        pg.mixer.music.stop()
        screen.blit(font_end.render('Score: ' + str(score), True, '#006400'), (50, 140))
        screen.blit(font_end.render('Best score: ' + str(best_score), True, '#006400'), (50, 230))


        if restart_button.draw(screen):
            pg.mixer.music.play(loops=-1)
            scream_sound_wasnt = True
            playing = True
            score = 0
            all_sprites = pg.sprite.Group()
            platforms = pg.sprite.Group()
            player = Player(screen)
            all_sprites.add(player)
            for plat in PLATFORM_LIST:
                p = Platform(*plat)
                all_sprites.add(p)
                platforms.add(p)

    clock.tick(60)

    pg.display.flip()
pg.quit()
