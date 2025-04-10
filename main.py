from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Snake')

class GameSprite(sprite.Sprite):
    def __init__(self, img,x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Snake(GameSprite):
    def __init__(self, img,x,y,w,h,t):
        super().__init__(img,x,y,w,h)
        self.type = t
        self.speed = 1
        self.direction = "0"
        self.cur_image = self.image
    
    def update(self):
        if self.direction == 'l':
            self.rect.x -= self.speed
        elif self.direction == 'r':
            self.rect.x += self.speed
        elif self.direction == 'u':
            self.rect.y -= self.speed
        elif self.direction == 'd':
            self.rect.y += self.speed
        keys = key.get_pressed()
        if keys[K_LEFT] and self.direction != 'r':
            self.direction = 'l'
            self.image = transform.rotate(self.cur_image, -90)
        if keys[K_RIGHT] and self.direction != 'l':
            self.direction = 'r'
            self.image = transform.rotate(self.cur_image, 90)
        if keys[K_UP] and self.direction != 'd':
            self.direction = 'u'
            self.image = transform.rotate(self.cur_image, 180)
        if keys[K_DOWN] and self.direction != 'u':
            self.direction = 'd'
            self.image = transform.rotate(self.cur_image, 0)
head = Snake('snakehead.png', 350, 250, 25,25, 0)
      
game = True
clock = time.Clock()
fps = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((0,0,0))

    head.update()
    head.reset()


    
    clock.tick(fps)
    display.update()