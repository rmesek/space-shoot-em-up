import pygame

from data.engine.defines import *

pygame.init()
pygame.mixer.init()


def main():
    # Play music
    pygame.mixer.music.load(SFX_DIR / "8bit_ost.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.40)


if __name__ == "__main__":
    main()

    pygame.quit()
