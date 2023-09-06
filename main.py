import pygame, sys, random

WINDOW_SIZE = WIN_W, WIN_H = (1280, 720)
DISPLAY_SIZE = W, H = (640, 360)
BLUE = (67, 156, 239)
FPS = 60

target_img = pygame.transform.scale_by(pygame.image.load('data/target.png'), 3)

class Target(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.pos = pos
        self.image = target_img.convert_alpha()
        self.rect = self.image.get_rect(center = self.pos)
    
    def click(self):
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.kill()
    
    def update(self):
        self.click()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Clicker")

        self.window = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
        self.clock = pygame.time.Clock()

        self.targets = pygame.sprite.Group()
        self.test = Target(self.rand_pos(), self.targets)
    
    def rand_pos(self):
        x = random.randint(50, W-50)
        y = random.randint(50, H-50)
        return pygame.Vector2(x, y)
    
    def quit(self):
        pygame.quit()
        sys.exit()
    
    def update(self):
        self.targets.update()

    def render(self):
        self.targets.draw(self.window)
    
    def run(self):
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            
            self.update()

            self.window.fill(BLUE)
            self.render()
            
            pygame.display.update()

Game().run()
