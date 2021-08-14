from pathlib import Path

# DIRECTORIES
GAME_DIR = Path(__file__).parents[3]
SRC_DIR = GAME_DIR / "src"
DATA_DIR = SRC_DIR / "data"
ENGINE_DIR = DATA_DIR / "engine"
SFX_DIR = DATA_DIR / "sfx"


if __name__ == "__main__":
    print(GAME_DIR)
    print(DATA_DIR)
    print(ENGINE_DIR)
