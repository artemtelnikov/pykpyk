from pygame import *
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()
window = display.set_mode((700, 500))
display.set_caption('ПИНАЙ АНДРЕЯ')
background = transform.scale(image.load('manface.jpg'), (700, 500))
win_width = 700
win_height = 500



window.blit(background, (0,0))

speed_x = 3
speed_y = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_image2, player_x, player_y, h,w, player_speed,):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (h, w))
        self.image2 = transform.scale(image.load(player_image), (h, w))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def reset(self):
        window.blit(self.image2, (self.rect.x, self.rect.y))

game = True


class Player(GameSprite):
    def __init__(self, player_image, player_image2, player_x,  player_y, h,w, player_speed):   
        super().__init__(player_image, player_image2, player_x, player_y, h,w, player_speed)
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_DOWN] and self.rect.y > -300:
            self.rect.y += 4
            
        if key_pressed[K_UP] and self.rect.y < 400:
            self.rect.y -= 4
class Player2(GameSprite):
    def __init__(self, player_image, player_image2, player_x, player_y, h,w, player_speed):   
        super().__init__(player_image, player_image2, player_x, player_y, h,w, player_speed)
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_s] and self.rect.y > -300:
            self.rect.y += 4
            
        if key_pressed[K_w] and self.rect.y < 500:
            self.rect.y -= 4



ballin = Player('vilka.jpg', 0, 0, 30, 100, 100, 100)
ballin2 = Player2('lozka.jpg', 0, 600, 30, 100, 100, 5)
ball = GameSprite('ball.png', 100, 100, 30, 50, 50, 5)
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > win_height:
        speed_y *= -1
    if ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(ballin, ball):
        speed_x *= -1
    if sprite.collide_rect(ballin2, ball):
        speed_x *= -1

    ballin.update()
    ballin.reset()
    ballin2.update()
    ballin2.reset()
    ball.update()
    ball.reset()
    display.update()
