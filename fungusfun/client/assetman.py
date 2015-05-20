import pygame
import os

cache = {}

def getImage(fn, useCache=True):
    if fn in cache and useCache:
        return cache[fn]

    img = pygame.image.load(os.path.join("fungusfun", "client", "assets", fn))
    cache[fn] = img

    return img