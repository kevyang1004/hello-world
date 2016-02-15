class Map(object):

    scenes = {
        'cent.corri.': CentralCorridor(),
        'LWA': LaserWeaponArmory(),
        'bridge': TheBridge(),
        'escape': EscapePod(),
        'death': Death(),
        'finish': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        pass

    def next_scene(self, scene_name):
        obj = Map.scenes.get(scene_name)
        return obj

    def opening_scene(self):
        return self.next_scene(self.start_scene)
        pass


a_map = Map('cent.corri.')
a_game = Engine(a_map)
a_game.play()
