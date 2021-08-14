import pygame


def load_img(file, directory, scale, convert_alpha=False):
    try:
        path = directory / file
        if not convert_alpha:
            img = pygame.image.load(path).convert_alpha()
        else:
            img = pygame.image.load(path).convert()
            trans_color = img.get_at((0, 0))
            img.set_colorkey(trans_color)
        img_w = img.get_width()
        img_h = img.get_height()
        img = pygame.transform.scale(img, (img_w*scale, img_h*scale))
        return img
    except Exception as e:
        print(f"ERROR loading {file}: {e}. Loading default texture instead.")
        s = pygame.Surface((32, 32))
        s.fill('red')
        return s
