import pygame

from .defines import *
from .widgets import *
from .funcs import (
    load_image,
    load_sound,
    draw_background,
)


# TITLE SCENE
class TitleScene:  # class TitleScene(Scene):
    def __init__(self, user_data):
        # Player preferences
        self.user_data = user_data

        # Background
        self.BG_IMG = load_image("background.png", IMG_DIR, SCALE)
        self.bg_rect = self.BG_IMG.get_rect()
        self.bg_y = 0
        self.PAR_IMG = load_image("background_parallax.png", IMG_DIR, SCALE)
        self.par_rect = self.BG_IMG.get_rect()
        self.par_y = 0

        # Images
        self.logo_img = load_image("logo_notilt.png", IMG_DIR, 4, convert_alpha=False)
        self.logo_rect = self.logo_img.get_rect()
        self.logo_hw = self.logo_rect.width / 2

        # Menu object
        self.title_menu = TitleMenuWidget(self.user_data.title_selected)

        # Logo bob
        self.bob_timer = pygame.time.get_ticks()
        self.bob_m = 0

        self.exit = False

        # Sounds
        self.sfx_keypress = load_sound("sfx_keypress.wav", SFX_DIR, self.user_data.sfx_vol)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:

                if event.key == self.user_data.key_up:
                    self.title_menu.select_up()
                    self.sfx_keypress.play()  # Play key press sound

                elif event.key == self.user_data.key_down:
                    self.title_menu.select_down()
                    self.sfx_keypress.play()

    def update(self, dt):
        self.bg_y += BG_SPD * dt
        self.par_y += PAR_SPD * dt
        self.title_menu.update()

    def draw(self, window):
        now = pygame.time.get_ticks()
        if now - self.bob_timer > 500:
            self.bob_timer = now
            self.bob_m = 1 - self.bob_m

        draw_background(window, self.BG_IMG, self.bg_rect, self.bg_y)
        draw_background(window, self.PAR_IMG, self.par_rect, self.par_y)
        window.blit(self.logo_img, (WIN_RES["w"]/2 - self.logo_hw, -64 + (2*self.bob_m)))

        # Draw menu
        self.title_menu.draw(window)
        draw_text(window, f"Game v{VERSION}", int(FONT_SIZE / 2), FONT_FILE, window.get_rect().centerx,
                  window.get_rect().bottom - 32, "WHITE", "centered")
        draw_text(window, "Pygame v2.0.1", int(FONT_SIZE / 2), FONT_FILE, window.get_rect().centerx,
                  window.get_rect().bottom - 24, "WHITE", "centered")
        draw_text(window, "Code licensed under GPL-3.0", int(FONT_SIZE / 2), FONT_FILE, window.get_rect().centerx,
                  window.get_rect().bottom - 16, "WHITE", "centered")
        draw_text(window, "Art licensed under CC BY-NC 4.0", int(FONT_SIZE / 2), FONT_FILE, window.get_rect().centerx,
                  window.get_rect().bottom-8, "WHITE", "centered")
