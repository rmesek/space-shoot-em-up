import pygame


# SCENES & MANAGERS

class SceneManager:
    def __init__(self, init_scene):
        self.scene = None
        self.go_to(init_scene)

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self


# ASSET LOADING / SAVING

def load_image(filename, directory, scale, convert_alpha=False):
    try:
        path = directory / filename
        if not convert_alpha:
            img = pygame.image.load(path).convert_alpha()
        else:
            img = pygame.image.load(path).convert()
            trans_color = img.get_at((0, 0))
            img.set_colorkey(trans_color)
        img_w = img.get_width()
        img_h = img.get_height()
        img = pygame.transform.scale(img, (img_w * scale, img_h * scale))
        return img
    except Exception as e:
        print(f"ERROR loading {filename}: {e}. Loading default texture instead.")
        s = pygame.Surface((32, 32))
        s.fill('red')
        return s


def load_sound(filename, directory, volume):
    path = directory / filename
    snd = pygame.mixer.Sound(path)
    snd.set_volume(volume)
    return snd


# DRAWING

def draw_background(surf, img, img_rect, ypos):
    surf_h = surf.get_height()
    rel_y = ypos % img_rect.height
    surf.blit(img, (0, rel_y - img_rect.height))

    if rel_y < surf_h:
        surf.blit(img, (0, rel_y))


def draw_text(surf, text, size, font, x, y, color, align="normal"):
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if align == "centered":
        text_rect.centerx = x
        text_rect.y = y
    elif align == "normal":
        text_rect.x = x
        text.rect.y = y
    surf.blit(text_surface, (text_rect.x, text_rect.y))


def draw_text2(surf, text, font, font_size, position, color, align="normal", italic=False):
    # Just a function with slightly better argument formatting and functionalities

    # Create Font object
    font = pygame.font.Font(font, font_size)

    # Italic settings
    if italic:
        font.italic = True

    # Create surface
    text_surface = font.render(text, True, color)

    # Find dest
    dest = [0, 0]
    if align == "normal":
        dest[0] = position[0]
        dest[1] = position[1]
    elif align == "center":
        dest[0] = surf.get_width() / 2 - text_surface.get_width() / 2
        dest[1] = position[1]

    # Display text on surface
    surf.blit(text_surface, dest)


def image_at(spritesheet, rectangle, convert_alpha=False):
    # Code stolen from the pygame wiki and modified for personal use. The boons of open source!
    rect = pygame.Rect(rectangle)
    image = pygame.Surface(rect.size).convert_alpha()
    image.blit(spritesheet, (0, 0), rect)
    if convert_alpha:
        image.set_colorkey("BLACK")
    return image


def scale_rect(scale, rect):
    scaled = map((lambda x: x * scale), rect)
    return tuple(scaled)
