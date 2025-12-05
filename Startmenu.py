import pygame
import sys

pygame.init()

# --- Window settings ---
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BLOOD HUNT - Startmenü")

# --- Musik laden und abspielen ---
pygame.mixer.music.load("mixkit-tapis-615.mp3")
pygame.mixer.music.set_volume(0.5)  # Lautstärke (0.0 - 1.0)
pygame.mixer.music.play(-1)         # -1 = Endlosschleife

# --- Colors ---
WHITE = (255, 255, 255)
RED = (180, 40, 40)
BLACK = (0, 0, 0)
GRAY = (80, 80, 80)

# --- Fonts ---
title_font = pygame.font.SysFont("timesnewroman", 70, bold=True)
subtitle_font = pygame.font.SysFont("timesnewroman", 32, italic=True)
button_font = pygame.font.SysFont("arial", 35)

# --- Button class ---
class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, GRAY, self.rect, border_radius=8)
        else:
            pygame.draw.rect(screen, BLACK, self.rect, border_radius=8)

        text_surf = button_font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# --- Buttons ---
buttons = [
    Button("Start", 350, 250, 200, 50),
    Button("Speichern", 350, 310, 200, 50),
    Button("Laden", 350, 370, 200, 50),
    Button("Option", 350, 430, 200, 50),
    Button("Beenden", 350, 490, 200, 50),
]

# --- Main loop ---
def main():
    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in buttons:
                    if btn.is_clicked(mouse_pos):
                        if btn.text == "Start":
                            print("Spiel startet…")
                        elif btn.text == "Speichern":
                            print("Spiel speichern…")
                        elif btn.text == "Laden":
                            print("Spiel laden…")
                        elif btn.text == "Option":
                            print("Optionsmenü…")
                        elif btn.text == "Beenden":
                            pygame.quit()
                            sys.exit()

        # --- Drawing ---
        screen.fill((20, 20, 20))

        title = title_font.render("BLOOD HUNT", True, RED)
        subtitle = subtitle_font.render("GARDEN OF ROSES AND SORROWS", True, WHITE)

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 80))
        screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, 160))

        for btn in buttons:
            btn.draw(screen, mouse_pos)

        pygame.display.update()


if __name__ == "__main__":
    main()
