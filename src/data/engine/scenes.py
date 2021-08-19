import pygame

from .defines import *
from .widgets import *
from .funcs import (
    load_image,
    load_sound,
    draw_background,
    SceneManager,
    draw_text
)


# TITLE SCENE
class TitleScene:  # class TitleScene(Scene):
    def __init__(self, user_data):
        self.manager = None
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

                elif event.key == self.user_data.key_fire or event.key == pygame.K_RETURN:
                    self.sfx_keypress.play()  # Play key press sound

                    if self.title_menu.get_selected() == 0:
                        pass

                    elif self.title_menu.get_selected() == 1:
                        pass

                    elif self.title_menu.get_selected() == 2:
                        self.user_data.title_selected = 2
                        self.manager.go_to(OptionsScene(self.user_data))

                    elif self.title_menu.get_selected() == 3:
                        pass

                    elif self.title_menu.get_selected() == 4:
                        self.exit = True

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
        window.blit(self.logo_img, (WIN_RES["w"] / 2 - self.logo_hw, -64 + (2 * self.bob_m)))

        # Draw menu
        self.title_menu.draw(window)
        draw_text(window, f"Game v{VERSION}", int(FONT_SIZE / 2), FONT_FILE, window.get_rect().centerx,
                  window.get_rect().bottom - 32, "WHITE", "centered")
        draw_text(window, "Pygame v2.0.1", int(FONT_SIZE / 2), FONT_FILE, window.get_rect().centerx,
                  window.get_rect().bottom - 24, "WHITE", "centered")
        draw_text(window, "Code licensed under GPL-3.0", int(FONT_SIZE / 2), FONT_FILE, window.get_rect().centerx,
                  window.get_rect().bottom - 16, "WHITE", "centered")
        draw_text(window, "Art licensed under CC BY-NC 4.0", int(FONT_SIZE / 2), FONT_FILE, window.get_rect().centerx,
                  window.get_rect().bottom - 8, "WHITE", "centered")


# OPTIONS SCENE

class OptionsScene:
    def __init__(self, user_data):
        self.manager = None
        self.user_data = user_data

        # Background
        self.BG_IMG = load_image("background.png", IMG_DIR, SCALE)
        self.bg_rect = self.BG_IMG.get_rect()
        self.bg_y = 0
        self.PAR_IMG = load_image("background_parallax.png", IMG_DIR, SCALE)
        self.par_rect = self.BG_IMG.get_rect()
        self.par_y = 0

        # Menu widget
        self.menu_widget = OptionsSceneMenuWidget(self.user_data.options_scene_selected)

        # Sounds
        self.sfx_keypress = load_sound("sfx_keypress.wav", SFX_DIR, self.user_data.sfx_vol)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:

                # Key press events
                if event.key == self.user_data.key_back:
                    self.sfx_keypress.play()  # Play key press sound
                    self.user_data.options_scene_selected = 0
                    self.manager.go_to(TitleScene(self.user_data))

                elif event.key == self.user_data.key_up:
                    self.sfx_keypress.play()
                    self.menu_widget.select_up()

                elif event.key == self.user_data.key_down:
                    self.sfx_keypress.play()
                    self.menu_widget.select_down()

                elif event.key == self.user_data.key_fire or event.key == pygame.K_RETURN:
                    self.sfx_keypress.play()

                    if self.menu_widget.get_selected_str() == "VIDEO":
                        self.user_data.options_scene_selected = 0
                        self.manager.go_to(VideoOptionsScene(self.user_data))

                    elif self.menu_widget.get_selected_str() == "SOUND":
                        self.user_data.options_scene_selected = 1
                        self.manager.go_to(SoundOptionsScene(self.user_data))

                    elif self.menu_widget.get_selected_str() == "GAME":
                        self.user_data.options_scene_selected = 2
                        self.manager.go_to(GameOptionsScene(self.user_data))

                    elif self.menu_widget.get_selected_str() == "CONTROLS":
                        self.user_data.options_scene_selected = 3

                    elif self.menu_widget.get_selected_str() == "BACK":
                        self.user_data.options_scene_selected = 0
                        self.manager.go_to(TitleScene(self.user_data))

    def update(self, dt):
        self.bg_y += BG_SPD * dt
        self.par_y += PAR_SPD * dt

        self.menu_widget.update()

    def draw(self, window):
        draw_background(window, self.BG_IMG, self.bg_rect, self.bg_y)
        draw_background(window, self.PAR_IMG, self.par_rect, self.par_y)

        draw_text2(window, "OPTIONS", FONT_FILE, FONT_SIZE*2, (WIN_RES["w"]/2, 64), "WHITE", "center")
        self.menu_widget.draw(window)


class VideoOptionsScene:
    def __init__(self, user_data):
        self.manager = None
        self.user_data = user_data

        # Background
        self.BG_IMG = load_image("background.png", IMG_DIR, SCALE)
        self.bg_rect = self.BG_IMG.get_rect()
        self.bg_y = 0
        self.PAR_IMG = load_image("background_parallax.png", IMG_DIR, SCALE)
        self.par_rect = self.BG_IMG.get_rect()
        self.par_y = 0

        # Menu widget
        self.menu_widget = VideoOptionsSceneMenuWidget(self.user_data)

        # Sounds
        self.sfx_keypress = load_sound("sfx_keypress.wav", SFX_DIR, self.user_data.sfx_vol)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:

                # Key press events
                if event.key == self.user_data.key_fire or event.key == pygame.K_RETURN:
                    self.sfx_keypress.play()  # Play key press sound

                    if self.menu_widget.get_selected() == self.menu_widget.get_max_index():
                        self.manager.go_to(OptionsScene(self.user_data))

                elif event.key == self.user_data.key_back:
                    self.sfx_keypress.play()
                    self.manager.go_to(OptionsScene(self.user_data))

                elif event.key == self.user_data.key_up:
                    self.sfx_keypress.play()
                    self.menu_widget.select_up()

                elif event.key == self.user_data.key_down:
                    self.sfx_keypress.play()
                    self.menu_widget.select_down()

                elif event.key == self.user_data.key_left:
                    self.sfx_keypress.play()
                    self.menu_widget.select_left()

                elif event.key == self.user_data.key_right:
                    self.sfx_keypress.play()
                    self.menu_widget.select_right()

    def update(self, dt):
        self.bg_y += BG_SPD * dt
        self.par_y += PAR_SPD * dt

        self.menu_widget.update()

    def draw(self, window):
        draw_background(window, self.BG_IMG, self.bg_rect, self.bg_y)
        draw_background(window, self.PAR_IMG, self.par_rect, self.par_y)

        draw_text2(window, "VIDEO OPTIONS", FONT_FILE, FONT_SIZE*2, (WIN_RES["w"]/2, 64), "WHITE", "center")
        self.menu_widget.draw(window)


class SoundOptionsScene:
    def __init__(self, user_data):
        self.manager = None
        self.user_data = user_data

        # Background
        self.BG_IMG = load_image("background.png", IMG_DIR, SCALE)
        self.bg_rect = self.BG_IMG.get_rect()
        self.bg_y = 0
        self.PAR_IMG = load_image("background_parallax.png", IMG_DIR, SCALE)
        self.par_rect = self.BG_IMG.get_rect()
        self.par_y = 0

        # Menu widget
        self.menu_widget = SoundOptionsSceneMenuWidget(self.user_data)

        # Key press delay
        self.press_timer = pygame.time.get_ticks()
        self.press_delay = 75

        # Sounds
        self.sfx_keypress = load_sound("sfx_keypress.wav", SFX_DIR, self.user_data.sfx_vol)

    def handle_events(self, events):
        # Key down events
        for event in events:
            if event.type == pygame.KEYDOWN:

                if event.key == self.user_data.key_fire or event.key == pygame.K_RETURN:
                    self.sfx_keypress.play()

                    if self.menu_widget.get_selected() == self.menu_widget.get_max_index():
                        self.manager.go_to(OptionsScene(self.user_data))

                elif event.key == self.user_data.key_back:
                    self.sfx_keypress.play()
                    self.manager.go_to(OptionsScene(self.user_data))

                elif event.key == self.user_data.key_up:
                    self.sfx_keypress.play()
                    self.menu_widget.select_up()

                elif event.key == self.user_data.key_down:
                    self.sfx_keypress.play()
                    self.menu_widget.select_down()

        # Volume knob key presses
        now = pygame.time.get_ticks()
        if now - self.press_timer > self.press_delay:
            self.press_timer = now

            pressed = pygame.key.get_pressed()
            if pressed[self.user_data.key_left]:
                self.menu_widget.select_left()

            elif pressed[self.user_data.key_right]:
                self.menu_widget.select_right()

    def update(self, dt):
        self.bg_y += BG_SPD * dt
        self.par_y += PAR_SPD * dt

        # Update preferences
        self.user_data.sfx_vol = self.menu_widget.rs_sfx.get_value() / 100
        self.user_data.music_vol = self.menu_widget.rs_ost.get_value() / 100

        # Update sound volumes
        self.sfx_keypress.set_volume(self.user_data.sfx_vol)

        self.menu_widget.update()

    def draw(self, window):
        draw_background(window, self.BG_IMG, self.bg_rect, self.bg_y)
        draw_background(window, self.PAR_IMG, self.par_rect, self.par_y)

        draw_text2(window, "SOUND OPTIONS", FONT_FILE, FONT_SIZE*2, (WIN_RES["w"]/2, 64), "WHITE", "center")
        self.menu_widget.draw(window)


class GameOptionsScene:
    def __init__(self, user_data):
        self.manager = None
        self.user_data = user_data

        # Background
        self.BG_IMG = load_image("background.png", IMG_DIR, SCALE)
        self.bg_rect = self.BG_IMG.get_rect()
        self.bg_y = 0
        self.PAR_IMG = load_image("background_parallax.png", IMG_DIR, SCALE)
        self.par_rect = self.BG_IMG.get_rect()
        self.par_y = 0

        # Menu widget
        self.menu_widget = GameOptionsSceneMenuWidget(self.user_data)

        # Sounds
        self.sfx_keypress = load_sound("sfx_keypress.wav", SFX_DIR, self.user_data.sfx_vol)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:

                if event.key == self.user_data.key_fire or event.key == pygame.K_RETURN:
                    self.sfx_keypress.play()
                    if self.menu_widget.get_selected() == self.menu_widget.get_max_index():
                        self.manager.go_to(OptionsScene(self.user_data))

                elif event.key == self.user_data.key_back:
                    self.sfx_keypress.play()
                    self.manager.go_to(OptionsScene(self.user_data))

                elif event.key == self.user_data.key_up:
                    self.sfx_keypress.play()
                    self.menu_widget.select_up()

                elif event.key == self.user_data.key_down:
                    self.sfx_keypress.play()
                    self.menu_widget.select_down()

                elif event.key == self.user_data.key_left:
                    self.sfx_keypress.play()
                    self.menu_widget.select_left()

                elif event.key == self.user_data.key_right:
                    self.sfx_keypress.play()
                    self.menu_widget.select_right()

    def update(self, dt):
        self.bg_y += BG_SPD * dt
        self.par_y += PAR_SPD * dt

        self.menu_widget.update()

    def draw(self, window):
        draw_background(window, self.BG_IMG, self.bg_rect, self.bg_y)
        draw_background(window, self.PAR_IMG, self.par_rect, self.par_y)

        draw_text2(window, "GAME OPTIONS", FONT_FILE, FONT_SIZE*2, (WIN_RES["w"]/2, 64), "WHITE", "center")
        self.menu_widget.draw(window)
