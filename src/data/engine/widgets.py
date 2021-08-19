import pygame

from .defines import *
from .funcs import (
    load_image,
    load_sound,
    draw_text2,
)


# Title Scene Widgets
class TitleMenuWidget:
    def __init__(self, init_selected):
        # Surface
        # Warning - options may go beyond the surface and will be not rendered
        self.surface = pygame.Surface((WIN_RES["w"], 350))
        self.surf_rect = self.surface.get_rect()

        self.spacing = FONT_SIZE / 2

        # Menu
        self.options = ("PLAY", "SCORES", "OPTIONS", "CREDITS", "EXIT")
        self.act_opt = [0 for _ in range(len(self.options))]  # Active options
        self.act_opt[init_selected] = 1
        self.colors = {0: "white", 1: "black"}  # Colors for active/inactive menu

        # Selector
        self.selector = pygame.Surface((WIN_RES["w"], FONT_SIZE + 4))
        self.selector.fill("white")
        self.sel_y = FONT_SIZE + self.spacing
        self.sel_i = init_selected  # Index

    def update(self):
        self.sel_y = FONT_SIZE * (self.sel_i + 1) + self.spacing * (self.sel_i + 1)

    def draw(self, window):
        self.surface.fill("black")
        self.surface.set_colorkey("black")
        self.surface.blit(self.selector, (0, self.sel_y - 3))
        for i in range(len(self.options)):
            draw_text2(self.surface, self.options[i], FONT_FILE, FONT_SIZE,
                       (self.surf_rect.centerx, FONT_SIZE * (i + 1) + self.spacing * (i + 1)),
                       self.colors[self.act_opt[i]], "center")
        window.blit(self.surface, (0, window.get_height() / 2 - 32))

    def select_up(self):
        if self.sel_i > 0:
            self.act_opt[self.sel_i] = 0
            self.sel_i -= 1
            self.act_opt[self.sel_i] = 1
        else:
            self.act_opt[self.sel_i] = 0
            self.sel_i = len(self.options) - 1
            self.act_opt[self.sel_i] = 1

    def select_down(self):
        if self.sel_i < len(self.options) - 1:
            self.act_opt[self.sel_i] = 0
            self.sel_i += 1
            self.act_opt[self.sel_i] = 1
        else:
            self.act_opt[self.sel_i] = 0
            self.sel_i = 0
            self.act_opt[self.sel_i] = 1

    def get_selected(self):
        return self.sel_i


class OptionsSceneMenuWidget:
    def __init__(self, init_selected=0):
        # Surface
        self.surface = pygame.Surface((WIN_RES["w"], 350))
        self.surf_rect = self.surface.get_rect()

        self.spacing = FONT_SIZE

        # Menu
        self.options = ("VIDEO", "SOUND", "GAME", "CONTROLS", "BACK")
        self.act_opt = [0 for _ in range(len(self.options))]  # Active options
        self.act_opt[init_selected] = 1
        self.colors = {0: "white", 1: "black"}  # Colors for active/inactive options

        # Selector
        self.selector = pygame.Surface((WIN_RES["w"], FONT_SIZE + 4))
        self.selector.fill("white")
        self.sel_y = FONT_SIZE + self.spacing
        self.sel_i = init_selected  # Index

        # Back button
        self.back_button = pygame.Surface((128, 32))

    def update(self):
        self.sel_y = FONT_SIZE * (self.sel_i + 1) + self.spacing * (self.sel_i + 1)

    def draw(self, window):
        self.back_button.fill("BLACK")
        self.back_button.set_colorkey("BLACK")
        self.surface.fill("black")
        self.surface.set_colorkey("black")

        # Change selector size and draw
        if self.options[self.sel_i] != "BACK":
            self.selector = pygame.Surface((WIN_RES["w"], FONT_SIZE + 4))
            self.selector.fill("white")
            self.surface.blit(self.selector, (0, self.sel_y - 3))
        else:
            self.selector = pygame.Surface((128, 32))
            self.selector.fill("white")
            self.back_button.blit(
                self.selector,
                (0, 0)
            )

        # Draw menu
        for i in range(len(self.options)):
            if self.options[i] != "BACK":
                draw_text2(self.surface, self.options[i], FONT_FILE, FONT_SIZE,
                           (self.surf_rect.centerx, FONT_SIZE * (i + 1) + self.spacing * (i + 1)),
                           self.colors[self.act_opt[i]], "center")
            else:
                draw_text2(self.back_button, "BACK", FONT_FILE, FONT_SIZE,
                           (self.back_button.get_width() / 2, self.back_button.get_height() / 2 - FONT_SIZE / 2),
                           self.colors[self.act_opt[i]], "center")
                window.blit(self.back_button,
                            (window.get_width() / 2 - self.back_button.get_width() / 2, window.get_height() * 0.8))

        # Draw the menu widget surface
        window.blit(self.surface, (0, window.get_height() * 0.3))

    def select_up(self):
        if self.sel_i > 0:
            self.act_opt[self.sel_i] = 0
            self.sel_i -= 1
            self.act_opt[self.sel_i] = 1
        else:
            self.act_opt[self.sel_i] = 0
            self.sel_i = len(self.options) - 1
            self.act_opt[self.sel_i] = 1

    def select_down(self):
        if self.sel_i < len(self.options) - 1:
            self.act_opt[self.sel_i] = 0
            self.sel_i += 1
            self.act_opt[self.sel_i] = 1
        else:
            self.act_opt[self.sel_i] = 0
            self.sel_i = 0
            self.act_opt[self.sel_i] = 1

    def get_selected(self):
        return self.sel_i

    def get_selected_str(self):
        return self.options[self.sel_i]


class TextSelector:
    def __init__(self, init_value, options, position, alignment="LEFT", active=False):
        self.options = options
        self.alignment = alignment
        self.index = init_value
        self.ts_surf = pygame.Surface((64, 32))
        self.position = position
        self.active = active

        # Arrow animations
        self.jut_m = 0  # Jut multiplier for the arrows
        self.jut_timer = pygame.time.get_ticks()
        self.jut_delay = 500

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.jut_timer > self.jut_delay:
            self.jut_timer = now
            self.jut_m = 1 - self.jut_m  # Toggle between 0 and 1

    def draw(self, surface):
        # Automatically resize surface depending on text size
        text_length = len(self.options[self.index])
        surf_length = (text_length + 2) * FONT_SIZE
        self.ts_surf = pygame.Surface((surf_length, 32))

        self.ts_surf.fill("BLACK")
        self.ts_surf.set_colorkey("BLACK")

        if self.active:
            draw_text2(self.ts_surf, "<", FONT_FILE, FONT_SIZE,
                       (FONT_SIZE / 2 - (2 * self.jut_m),
                        self.ts_surf.get_height() / 2 - FONT_SIZE / 2),
                       "WHITE")
            draw_text2(self.ts_surf, ">", FONT_FILE, FONT_SIZE,
                       (self.ts_surf.get_width() - FONT_SIZE + (2 * self.jut_m),
                        self.ts_surf.get_height() / 2 - FONT_SIZE / 2),
                       "WHITE")

        # Draw text
        draw_text2(self.ts_surf, self.options[self.index], FONT_FILE, FONT_SIZE,
                   (0, self.ts_surf.get_height() / 2 - FONT_SIZE / 2),
                   "WHITE", align="center")

        # Draw selector to surface
        if self.alignment == "CENTER":
            surface.blit(self.ts_surf,
                         (surface.get_width() / 2 - self.ts_surf.get_width() / 2 + self.position[0],
                          self.position[1]))

    def go_left(self):
        if self.index <= 0:
            self.index = len(self.options) - 1
        else:
            self.index -= 1

    def go_right(self):
        if self.index >= len(self.options) - 1:
            self.index = 0
        else:
            self.index += 1

    def get_selected(self):
        return self.index

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False


class Button:
    def __init__(self, text, size, position):
        self.image = pygame.Surface(size)
        self.text = text
        self.position = position
        self.active = False
        self.text_color = "WHITE"
        self.surface_color = "BLACK"

    def update(self):
        pass

    def draw(self, surface):
        self.image.fill(self.surface_color)
        self.image.set_colorkey("BLACK")

        # Draw text
        draw_text2(self.image, self.text, FONT_FILE, FONT_SIZE,
                   (self.image.get_width() / 2, self.image.get_height() / 2 - FONT_SIZE / 2),
                   self.text_color,
                   align="center"
                   )
        surface.blit(self.image, self.position)

    def activate(self):
        self.text_color = "BLACK"
        self.surface_color = "WHITE"
        self.active = True

    def deactivate(self):
        self.text_color = "WHITE"
        self.surface_color = "BLACK"
        self.active = False


class VideoOptionsSceneMenuWidget:
    def __init__(self, user_data):
        self.user_data = user_data
        self.image = pygame.Surface((WIN_RES["w"], 350))
        x_alignment = self.image.get_width() * 0.30
        btn_x_size = 128

        # Options
        self.ts_fullscreen_y = 16
        self.ts_frameless_y = 64
        self.ts_fullscreen = TextSelector(self.user_data.is_fullscreen, YESNO_OPTIONS,
                                          (x_alignment, self.ts_fullscreen_y), alignment="CENTER", active=True)
        self.ts_frameless = TextSelector(self.user_data.is_frameless, YESNO_OPTIONS,
                                         (x_alignment, self.ts_frameless_y), alignment="CENTER")
        self.btn_back = Button("BACK", (btn_x_size, 32),
                               (self.image.get_width() / 2 - btn_x_size / 2, self.image.get_height() * 0.7))

        # Options list
        self.options = (self.ts_fullscreen, self.ts_frameless, self.btn_back)
        # Note: Back buttons should always be put at the last index of an options list
        self.MAX_OPTIONS = len(self.options)
        self.index = 0

        # To display the disclaimer
        self.settings_changed = False

    def update(self):
        for option in self.options:
            option.update()

        # Update preferences
        self.user_data.is_fullscreen = self.ts_fullscreen.get_selected()
        self.user_data.is_frameless = self.ts_frameless.get_selected()

    def draw(self, window):
        self.image.fill("BLACK")
        self.image.set_colorkey("BLACK")

        # Draw Labels
        draw_text2(self.image, "FULLSCREEN", FONT_FILE, FONT_SIZE,
                   (32, self.ts_fullscreen_y + FONT_SIZE / 2),
                   "WHITE")
        draw_text2(self.image, "FRAMELESS", FONT_FILE, FONT_SIZE,
                   (32, self.ts_frameless_y + FONT_SIZE / 2),
                   "WHITE")

        # Draw text selectors
        for option in self.options:
            option.draw(self.image)

        # Draw disclaimer
        if self.settings_changed:
            draw_text2(self.image, "Please restart the game", FONT_FILE, FONT_SIZE,
                       (32, self.image.get_height() * 0.4),
                       "WHITE", align="center")
            draw_text2(self.image, "to apply changes.", FONT_FILE, FONT_SIZE,
                       (32, self.image.get_height() * 0.45),
                       "WHITE", align="center")

        # Draw the widget to the screen
        window.blit(self.image, (0, window.get_height() * 0.3))

    def select_up(self):
        # Deactivate current text selector
        selected_option = self.options[self.index]
        selected_option.deactivate()

        # Move current text selector
        if self.index <= 0:
            self.index = self.MAX_OPTIONS - 1
        else:
            self.index -= 1

        # Activate current text selector
        selected_option = self.options[self.index]
        selected_option.activate()

    def select_down(self):
        # Deactivate current text selector
        selected_option = self.options[self.index]
        selected_option.deactivate()

        # Move current text selector
        if self.index >= self.MAX_OPTIONS - 1:
            self.index = 0
        else:
            self.index += 1

        # Activate current text selector
        selected_option = self.options[self.index]
        selected_option.activate()

    def select_left(self):
        selected_option = self.options[self.index]
        option_type = type(selected_option)
        if option_type == TextSelector:
            selected_option.go_left()

        if not self.settings_changed:
            self.settings_changed = True

    def select_right(self):
        selected_option = self.options[self.index]
        option_type = type(selected_option)
        if option_type == TextSelector:
            selected_option.go_right()

        if not self.settings_changed:
            self.settings_changed = True

    def get_selected(self):
        return self.index

    def get_max_index(self):
        return self.MAX_OPTIONS - 1


class RangeSelector:
    def __init__(self, init_value, minmax, position, alignment="LEFT", active=False):
        self.min_ = minmax[0]
        self.max_ = minmax[1]
        self.value = init_value
        self.alignment = alignment
        self.index = 0
        self.ts_surf = pygame.Surface((64, 32))
        self.position = position
        self.active = active

        # Arrow animations
        self.jut_m = 0
        self.jut_timer = pygame.time.get_ticks()
        self.jut_delay = 500

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.jut_timer > self.jut_delay:
            self.jut_timer = now
            self.jut_m = 1 - self.jut_m

    def draw(self, surface):
        text_length = len(str(int(self.value)))
        surf_length = (text_length + 2) * FONT_SIZE
        self.ts_surf = pygame.Surface((surf_length, 32))

        self.ts_surf.fill("BLACK")
        self.ts_surf.set_colorkey("BLACK")

        if self.active:
            # Draw the arrows
            if self.value > 0:
                draw_text2(self.ts_surf, "<", FONT_FILE, FONT_SIZE,
                           (FONT_SIZE / 2 - (2 * self.jut_m),
                            self.ts_surf.get_height() / 2 - FONT_SIZE / 2),
                           "WHITE"
                           )

            if self.value < self.max_:
                draw_text2(self.ts_surf, ">", FONT_FILE, FONT_SIZE,
                           (self.ts_surf.get_width() - FONT_SIZE + (2 * self.jut_m),
                            self.ts_surf.get_height() / 2 - FONT_SIZE / 2),
                           "WHITE"
                           )

        # Draw text
        draw_text2(self.ts_surf, str(int(self.value)), FONT_FILE, FONT_SIZE,
                   (0, self.ts_surf.get_height() / 2 - FONT_SIZE / 2),
                   "WHITE", align="center"
                   )

        # Draw selector to surface
        if self.alignment == "CENTER":
            surface.blit(self.ts_surf,
                         (surface.get_width() / 2 - self.ts_surf.get_width() / 2 + self.position[0], self.position[1])
                         )

    def decrease(self):
        if self.value <= self.min_:
            self.value = 0
        else:
            self.value -= 1

    def increase(self):
        if self.value >= self.max_:
            self.value = self.max_
        else:
            self.value += 1

    def get_value(self):
        return self.value

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False


class SoundOptionsSceneMenuWidget:
    def __init__(self, user_data):
        self.user_data = user_data
        self.image = pygame.Surface((WIN_RES["w"], 350))
        x_alignment = self.image.get_width() * 0.30
        btn_x_size = 128

        # Options
        self.rs_sfx_y = 16
        self.rs_ost_y = 64
        self.rs_sfx = RangeSelector(self.user_data.sfx_vol * 100, SFX_RANGE, (x_alignment, self.rs_sfx_y),
                                    alignment="CENTER", active=True)
        self.rs_ost = RangeSelector(self.user_data.music_vol * 100, MUSIC_RANGE, (x_alignment, self.rs_ost_y),
                                    alignment="CENTER")
        self.btn_back = Button("BACK", (btn_x_size, 32),
                               (self.image.get_width() / 2 - btn_x_size / 2, self.image.get_height() * 0.7))

        # Options list
        self.options = (self.rs_sfx, self.rs_ost, self.btn_back)
        self.MAX_OPTIONS = len(self.options)
        self.index = 0

        # Sounds
        self.sfx_keypress = load_sound("sfx_keypress.wav", SFX_DIR, self.user_data.sfx_vol)

    def update(self):
        for option in self.options:
            option.update()

        # Update preferences
        self.user_data.sfx_vol = self.rs_sfx.get_value() / 100
        self.user_data.music_vol = self.rs_ost.get_value() / 100

        # Update sound volumes
        self.sfx_keypress.set_volume(self.user_data.sfx_vol)

        pygame.mixer.music.set_volume(self.user_data.music_vol)

    def draw(self, window):
        self.image.fill("BLACK")
        self.image.set_colorkey("BLACK")

        # Draw labels
        draw_text2(self.image, "SFX", FONT_FILE, FONT_SIZE, (32, self.rs_sfx_y + FONT_SIZE / 2), "WHITE")
        draw_text2(self.image, "MUSIC", FONT_FILE, FONT_SIZE, (32, self.rs_ost_y + FONT_SIZE / 2), "WHITE")

        # Draw text selectors
        for option in self.options:
            option.draw(self.image)

        # Draw the widget to the screen
        window.blit(self.image, (0, window.get_height() * 0.3))

    def select_up(self):
        # Deactivate current text selector
        selected_option = self.options[self.index]
        selected_option.deactivate()

        # Move current text selector
        if self.index <= 0:
            self.index = self.MAX_OPTIONS - 1
        else:
            self.index -= 1

        # Activate current text selector
        selected_option = self.options[self.index]
        selected_option.activate()

    def select_down(self):
        # Deactivate current text selector
        selected_option = self.options[self.index]
        selected_option.deactivate()

        # Move current text selector
        if self.index >= self.MAX_OPTIONS - 1:
            self.index = 0
        else:
            self.index += 1

        # Activate current text selector
        selected_option = self.options[self.index]
        selected_option.activate()

    def select_left(self):
        selected_option = self.options[self.index]
        option_type = type(selected_option)
        if option_type == RangeSelector:
            # Play sound
            if selected_option.get_value() > selected_option.min_:
                self.sfx_keypress.play()

            # Decrease value
            selected_option.decrease()

    def select_right(self):
        selected_option = self.options[self.index]
        option_type = type(selected_option)
        if option_type == RangeSelector:
            # Play sound
            if selected_option.get_value() > selected_option.min_:
                self.sfx_keypress.play()

            selected_option.increase()

    def get_selected(self):
        return self.index

    def get_max_index(self):
        return self.MAX_OPTIONS - 1
