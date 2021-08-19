from pathlib import Path

# WINDOW AND METADATA DEFINES
WIN_RES = {"w": 320, "h": 480}
TITLE = "Space Shoot 'em up"
VERSION = "0.4"

# GAME OPTIONS
HP_OPTIONS = ("CIRCLE", "SQUARE")
YESNO_OPTIONS = ("NO", "YES")
SFX_RANGE = (0, 100)
MUSIC_RANGE = (0, 100)

# DIRECTORIES
GAME_DIR = Path(__file__).parents[3]
SRC_DIR = GAME_DIR / "src"
DATA_DIR = SRC_DIR / "data"
FONT_DIR = DATA_DIR / "font"
ENGINE_DIR = DATA_DIR / "engine"
IMG_DIR = DATA_DIR / "img"
SFX_DIR = DATA_DIR / "sfx"
FONT_FILE = FONT_DIR / "04B_03__.TTF"
USERDATA_FILE = ENGINE_DIR / "_userdata.dat"

# LOOP DEFINES
FPS = 60
DEBUG_MODE = False

# BG AND PARALLAX DEFINES
BG_SPD = 25
PAR_SPD = 50

# FONT AND IMAGES DEFINES
SCALE = 2
FONT_SIZE = 16

if __name__ == "__main__":
    print(GAME_DIR)
    print(DATA_DIR)
    print(ENGINE_DIR)
