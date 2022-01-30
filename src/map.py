from dataclasses import dataclass
import pygame
import pytmx
import pyscroll


@dataclass
class Map:
    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup


class MapManager:

    def __init__(self, screen, player):
        self.maps = dict()
        self.current_map = "world"
        self.screen = screen
        self.player = player
        self.register_map("world")
        self.register_map("house")

    def register_map(self, name):
        # charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame(f"./map/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data, self.screen.get_size()
        )
        map_layer.zoom = 2

        # définir liste qui va stocker les rect de collision
        walls = []
        for obj in tmx_data.objects:
            if obj.name == "collision":
                walls.append(
                    pygame.Rect(
                        obj.x,
                        obj.y,
                        obj.width,
                        obj.height
                    )
                )

        # dessiner le groupe de calque
        group = pyscroll.PyscrollGroup(
            map_layer=map_layer,
            default_layer=5
        )
        group.add(self.player)

        # Creer un objet map
        self.maps[name] = Map(name, walls, group)

    def get_map(self):
        return self.maps[self.current_map]

    def get_group(self):
        return self.get_map().group

    def get_walls(self):
        return self.get_map().walls

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
