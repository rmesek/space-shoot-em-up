import pygame

from .defines import *
from .funcs import (
    load_image,
    load_sound,
    draw_text,
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
            draw_text(self.surface, self.options[i], FONT_SIZE, FONT_FILE, self.surf_rect.centerx,
                      FONT_SIZE * (i + 1) + self.spacing * (i + 1), self.colors[self.act_opt[i]], "centered")
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
                draw_text(self.surface, self.options[i], FONT_SIZE, FONT_FILE, self.surf_rect.centerx,
                          FONT_SIZE * (i + 1) + self.spacing * (i + 1), self.colors[self.act_opt[i]], "centered")
            else:
                draw_text(self.back_button, "BACK", FONT_SIZE, FONT_FILE, self.back_button.get_width() / 2,
                          self.back_button.get_height() / 2 - FONT_SIZE / 2, self.colors[self.act_opt[i]], "centered")
                window.blit(self.back_button,
                            (window.get_width() / 2 - self.back_button.get_width() / 2, window.get_height() * 0.8))

        # Draw the menu widget surface
        window.blit(self.surface, (0, window.get_height()*0.3))

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
