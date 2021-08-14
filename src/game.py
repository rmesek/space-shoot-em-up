import pygame
import os
import pickle
import time

from pygame.locals import *

from data.engine.defines import *

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()
pygame.mixer.init()


# Player Preferences
class UserData:
    def __init__(self):
        self.is_fullscreen = False
        self.is_frameless = False
        self.music_vol = 0.40
        self.sfx_vol = 0.30
        self.game_difficulty = 0
        self.hp_pref = 0
        self.can_pause = False

        # Controls
        self.key_up = pygame.K_UP
        self.key_down = pygame.K_DOWN
        self.key_left = pygame.K_LEFT
        self.key_right = pygame.K_RIGHT
        self.key_fire = pygame.K_z
        self.key_back = pygame.K_x

        self.score = 0
        self.title_selected = 0
        self.options_scene_selected = 0


# Game loop
def main():
    # Load / create UserData object
    userdata = None
    try:
        with open(USERDATA_FILE, 'rb') as f:
            userdata = pickle.load(f)

            # Reset these variables
            userdata.title_selected = 0
            userdata.options_scene_selected = 0

    except FileNotFoundError:
        userdata = UserData()

    # Play music
    pygame.mixer.music.load(SFX_DIR / "8bit_ost.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(userdata.music_vol)

    # Set windows flags
    window_flags = HWACCEL | DOUBLEBUF
    if userdata.is_fullscreen:
        window_flags = window_flags | FULLSCREEN
    if userdata.is_frameless:
        window_flags = window_flags | NOFRAME

    # Initialize the window
    window = None
    if userdata.is_fullscreen:
        window = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h),
                                         window_flags)
    else:
        w = int(WIN_RES["w"]) * SCALE
        h = int(WIN_RES["h"]) * SCALE
        window = pygame.display.set_mode((w, h), window_flags)

    pygame.display.set_caption(TITLE)
    pygame.mouse.set_visible(False)

    # Loop variables
    clock = pygame.time.Clock()
    running = True
    prev_time = time.time()
    dt = 0

    while running:
        window.fill("BLACK")

        # Lock FPS
        clock.tick(FPS)

        # Calculate delta time
        now = time.time()
        dt = now - prev_time
        prev_time = now

        # Check for QUIT event
        if pygame.event.get(QUIT):
            try:
                with open(USERDATA_FILE, 'wb') as f:
                    pickle.dump(userdata, f)
            except Exception as e:
                print("Failed to save.")
                print(e)

            running = False
            return


if __name__ == "__main__":
    main()

    pygame.quit()
