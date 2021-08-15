import pygame
import os
import pickle
import time

from pygame.locals import *

from data.engine.defines import *
from data.engine.scenes import *
from data.engine.funcs import (
    load_image,
    SceneManager,
)

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()
pygame.mixer.init()


# Player Preferences
class UserData:
    def __init__(self):
        self.is_fullscreen = True
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
    user_data = None
    try:
        with open(USERDATA_FILE, 'rb') as f:
            user_data = pickle.load(f)

            # Reset these variables
            user_data.title_selected = 0
            user_data.options_scene_selected = 0

    except FileNotFoundError:
        user_data = UserData()

    # Play music
    pygame.mixer.music.load(SFX_DIR / "8bit_ost.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(user_data.music_vol)

    # Set windows flags
    window_flags = HWACCEL | DOUBLEBUF
    if user_data.is_fullscreen:
        window_flags = window_flags | FULLSCREEN
    if user_data.is_frameless:
        window_flags = window_flags | NOFRAME

    # Initialize the window
    window = None
    if user_data.is_fullscreen:
        window = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h),
                                         window_flags)
    else:
        w = int(WIN_RES["w"]) * SCALE
        h = int(WIN_RES["h"]) * SCALE
        window = pygame.display.set_mode((w, h), window_flags)

    pygame.display.set_caption(TITLE)
    pygame.display.set_icon(load_image("icon.png", IMG_DIR, 1))
    pygame.mouse.set_visible(False)

    # Create a scene manager
    manager = SceneManager(TitleScene(user_data))

    # Create Render target
    render_target = pygame.Surface((WIN_RES["w"], WIN_RES["h"]))

    # Loop variables
    clock = pygame.time.Clock()
    running = True
    prev_time = time.time()
    dt = 0

    while running:
        window.fill("BLACK")

        # Lock FPS
        clock.tick(FPS)
        if DEBUG_MODE:
            pygame.display.set_caption(f"{TITLE} (FPS: {round(clock.get_fps(),2)})")

        # Calculate delta time
        now = time.time()
        dt = now - prev_time
        prev_time = now

        # Check for QUIT event
        if pygame.event.get(QUIT):
            # Save player settings
            try:
                with open(USERDATA_FILE, 'wb') as f:
                    pickle.dump(user_data, f)
            except Exception as e:
                print("Failed to save.")
                print(e)

            # Exit loop and function
            running = False
            return

        # Call scene methods
        manager.scene.handle_events(pygame.event.get())
        manager.scene.update(dt)
        manager.scene.draw(render_target)

        # Draw screen
        if (window_flags & FULLSCREEN) != 0:
            if window.get_height() <= window.get_width():
                yscale = window.get_height() / WIN_RES["h"]
                targety = int(WIN_RES["h"] * yscale)
                targetx = int(targety*2/3)
            else:
                xscale = window.get_width() / WIN_RES["w"]
                targetx = int(WIN_RES["w"] * xscale)
                targety = int(targetx*3/2)

            window.blit(pygame.transform.scale(render_target, (targetx, targety)),
                        (window.get_width() / 2 - targetx / 2,
                         window.get_height() / 2 - targety / 2))

        else:
            window.blit(pygame.transform.scale(render_target, (window.get_width(), window.get_height())), (0, 0))

        pygame.display.flip()


if __name__ == "__main__":
    # Run main
    main()

    pygame.quit()
