from pathlib import Path

# WINDOW AND METADATA DEFINES
WIN_RES = {"w": 320, "h": 480}
TITLE = "Space Shoot 'em up"

# DIRECTORIES
GAME_DIR = Path(__file__).parents[3]
SRC_DIR = GAME_DIR / "src"
DATA_DIR = SRC_DIR / "data"
ENGINE_DIR = DATA_DIR / "engine"
IMG_DIR = DATA_DIR / "img"
SFX_DIR = DATA_DIR / "sfx"
USERDATA_FILE = ENGINE_DIR / "_userdata.dat"

# LOOP DEFINES
FPS = 60
DEBUG_MODE = False

# FONT AND IMAGES DEFINES
SCALE = 2

if __name__ == "__main__":
    print(GAME_DIR)
    print(DATA_DIR)
    print(ENGINE_DIR)
