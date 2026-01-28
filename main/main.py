import pygame
import sys

# Configuration
WIDTH, HEIGHT = 450, 700
FPS = 60
ELIXIR_RATE = 0.5  # Elixir per second

class Unit:
    def __init__(self, x, y, color, speed, cost):
        self.rect = pygame.Rect(x, y, 35, 35)
        self.color = color
        self.speed = speed
        self.cost = cost

    def move(self):
        self.rect.y -= self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=5)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Clash Royale Remix Prototype")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)

    units = []
    elixir = 5.0

    while True:
        # 1. Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                # Spawn "Fast" Unit (Cost 3)
                if event.key == pygame.K_1 and elixir >= 3:
                    units.append(Unit(WIDTH//2 - 17, HEIGHT - 120, (0, 150, 255), 4, 3))
                    elixir -= 3
                # Spawn "Tank" Unit (Cost 5)
                if event.key == pygame.K_2 and elixir >= 5:
                    units.append(Unit(WIDTH//2 - 17, HEIGHT - 120, (0, 0, 150), 1.5, 5))
                    elixir -= 5

        # 2. Logic
        elixir = min(elixir + (ELIXIR_RATE / FPS), 10) # Cap elixir at 10
        for u in units[:]:
            u.move()
            if u.rect.bottom < 0:
                units.remove(u)

        # 3. Render
        screen.fill((40, 120, 40)) # Grass
        
        # Draw Lanes
        pygame.draw.rect(screen, (30, 100, 30), (WIDTH//4, 0, WIDTH//2, HEIGHT))
        
        # Draw HUD
        elixir_text = font.render(f"Elixir: {int(elixir)}", True, (255, 255, 255))
        screen.blit(elixir_text, (20, HEIGHT - 40))
        
        # Draw Units
        for u in units:
            u.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
