import pygame, sys, random

WINDOW_SIZE = W, H = (1280, 720)
BLUE = (67, 156, 239)
BROWN = (101,83,83)
FPS = 60
SPAWNTARGET = pygame.USEREVENT + 1
TARGET_LIFETIME = 5000

target_img = pygame.transform.scale_by(pygame.image.load('data/target.png'), 3)

class Target(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.pos = pos
        self.image = target_img.convert_alpha()
        self.rect = self.image.get_rect(center = self.pos)
        self.clicked = False
        self.init_time = pygame.time.get_ticks()
    
    def timer(self):
        if pygame.time.get_ticks() - self.init_time > TARGET_LIFETIME:
            self.kill()
    
    def click(self):
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.clicked = True
    
    def update(self):
        self.timer()
        self.click()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Clicker")

        self.window = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
        self.clock = pygame.time.Clock()

        self.start_time = pygame.time.get_ticks()

        self.spawn_rate = 500
        self.point = 0

        self.targets = pygame.sprite.Group()
    
    def spawn_target(self):
        Target(self.rand_pos(), self.targets)
    
    def rand_pos(self):
        x = random.randint(50, W-50)
        y = random.randint(50, H-50)
        return pygame.Vector2(x, y)
    
    def quit(self):
        print(self.point)
        pygame.quit()
        sys.exit()
    
    def update(self):
        for target in self.targets:
            target.update()
            if target.clicked:
                target.kill()
                self.point += 1
        
        if pygame.time.get_ticks() - self.start_time >= 10000:
            self.quit()

    def render(self):
        self.targets.draw(self.window)
    
    def run(self):
        pygame.time.set_timer(SPAWNTARGET, self.spawn_rate)
        while True:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == SPAWNTARGET:
                    self.spawn_target()
            
            self.update()

            self.window.fill(BLUE)
            self.render()
            
            pygame.display.update()

Game().run()
