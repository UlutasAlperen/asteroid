import pygame

class ScorePopup(pygame.sprite.Sprite):
    def __init__(self, x, y, points):
        super().__init__()
        self.position = pygame.math.Vector2(x, y)
        self.lifetime = 1.0
        self.points = points
        self.font = pygame.font.Font(None, 24)
        
    def update(self, dt):
        self.lifetime -= dt
        self.position.y -= 100 * dt 
        if self.lifetime <= 0:
            self.kill()
            
    def draw(self, screen):
        if self.lifetime > 0:
            alpha = int(255 * self.lifetime)
            text = self.font.render(f"+{self.points}", True, (255, 255, 255))
            text.set_alpha(alpha)
            screen.blit(text, (self.position.x, self.position.y))
